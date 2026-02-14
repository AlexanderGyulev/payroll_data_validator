from validations import Checks
from pathlib import Path

data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail05_dir = data_dir / "fail_05_missing_employee_1"

def test_missing_pay_elements_1_pass():
    result = Checks(str(pass_all_dir))
    problems = result.missing_employee_2()
    assert len(problems) == 0

def test_missing_pay_elements_1_fail():
    result = Checks(str(fail05_dir))
    problems = result.missing_employee_2()
    assert len(problems) == 0