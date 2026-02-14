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

        for element in required_fields:
            if element not in df.columns:
                self.problems.append(f"GTN.xlsx has at least 1 missing column: {element}.")
                break
        return self.problems

    def missing_employee_1(self):
        self.problems = []
        df_gtn = pd.read_excel(self.gtn_file)
        df_payrun = pd.read_excel(self.payrun_file)

        gtn_set = set(df_gtn["employee_id"].dropna())
        payrun_set = set(df_payrun["System Employee ID"].dropna())

        missing_employees = payrun_set - gtn_set

        if len(missing_employees) > 0:
            self.problems.append(f"Employees present in Payrun.xlsx but not in GTN.xlsx: {missing_employees}.")
        return self.problems

    def missing_employee_2(self):
        self.problems = []
        df_gtn = pd.read_excel(self.gtn_file)
        df_payrun = pd.read_excel(self.payrun_file)

        gtn_set = set(df_gtn["employee_id"].dropna())
        payrun_set = set(df_payrun["System Employee ID"].dropna())

        missing_employees = gtn_set - payrun_set

        if len(missing_employees) > 0:
            self.problems.append(f"Employees present in GTN.xlsx but not in Payrun.xlsx: {missing_employees}.")
        return self.problems



