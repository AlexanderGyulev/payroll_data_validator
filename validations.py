import pandas as pd
import json


class Checks:
    def __init__(self,data_folder):
        self.problems = []
        self.gtn_file = data_folder + "/GTN.xlsx"
        self.payrun_file = data_folder + "/Payrun.xlsx"
        self.mapping_file = data_folder + "/mapping.json"

    def check_file_type(self):
        self.problems = []
        try:
            pd.read_excel(self.gtn_file)
        except Exception as e:
            self.problems.append(f"GTN.xlsx cannot be opened: {str(e)}")
        return self.problems

    def check_line_breaks(self):
        self.problems = []
        df = pd.read_excel(self.gtn_file)
        # print(df.to_string())
        empty_rows = df.isna().all(axis=1)
        if empty_rows.any(): # are there any Trues?
            self.problems.append(f"GTN.xlsx contains empty rows.")
        return self.problems

    def check_headers_changed(self):
        self.problems = []
        required_fields = []
        first_dict = json.load(open(self.mapping_file))
        mappings_dict = first_dict["mappings"]

        for keys in mappings_dict.keys():
            final_dict = mappings_dict[keys]

            if final_dict["map"]:
                required_fields.append(final_dict["vendor"])

        df = pd.read_excel(self.gtn_file)
        issues_set = set()

        for element in required_fields:
            if element not in df.columns:
                issues_set.add(element)

        if issues_set:
            self.problems.append(f"GTN.xlsx has missing header columns: {issues_set}.")

        return self.problems

    def missing_employees(self):
        self.problems = []
        df_gtn = pd.read_excel(self.gtn_file)
        df_payrun = pd.read_excel(self.payrun_file)

        gtn_set = set(df_gtn["employee_id"].dropna())
        payrun_set = set(df_payrun["System Employee ID"].dropna())

        missing_in_gtn = payrun_set - gtn_set
        missing_in_payrun = gtn_set - payrun_set

        if missing_in_gtn:
            self.problems.append(f"Employees present in Payrun but missing in GTN: {missing_in_gtn}.")
        if missing_in_payrun:
            self.problems.append(f"Employees present in GTN but missing in Payrun: {missing_in_payrun}.")
        return self.problems

    def missing_pay_elements_1(self):
        self.problems = []
        expected_elements = set()
        actual_elements = set()

        first_dict = json.load(open(self.mapping_file))
        mappings_dict = first_dict["mappings"]
        not_used_list = first_dict["not_used"]

        for key in mappings_dict.keys():
            expected_elements.add(mappings_dict[key]["vendor"])
        for element in not_used_list:
            expected_elements.add(element["vendor"])

        df = pd.read_excel(self.gtn_file)

        for column in df.columns:
            #print(column)
            if "element" in column.lower():
                actual_elements.add(column)

        missing = actual_elements - expected_elements

        if missing:
            self.problems.append(f"GTN.xlsx contains unmapped elements: {missing}.")

        return self.problems

    def missing_pay_elements_2(self):
        self.problems = []
        first_dict = json.load(open(self.mapping_file))
        mappings_dict = first_dict["mappings"]
        df = pd.read_excel(self.gtn_file)
        issue_set = set()

        for key in mappings_dict.keys():
            if mappings_dict[key]["map"]:
                get_vendor = mappings_dict[key]["vendor"]
                if get_vendor is None or get_vendor == "":
                    issue_set.add(key)

            if issue_set:
                self.problems.append(f"Pay elements in Payrun file do not have valid mapping: {issue_set}.")

        return self.problems

    def are_pay_elements_numeric(self):
        self.problems = []
        df = pd.read_excel(self.gtn_file)

        pay_columns = df.columns[4:].tolist()
        issues_set = set()

        for element in pay_columns:
            curr_series = df[element]
            non_empty = curr_series.dropna()
            convert_series = pd.to_numeric(non_empty, errors="coerce")

            if pd.isna(convert_series).any():
                issues_set.add(element)

            if issues_set:
                self.problems.append(f"The following columns in GTN.xlsx contains non-numeric values: {issues_set}.")

        return self.problems













