from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail04_dir = data_dir / "fail_04_missing_employee_1"

def test_missing_employee_1_pass():
    result = Checks(str(pass_all_dir))
    problems = result.missing_employees()
    assert len(problems) == 0

def test_missing_employee_1_fail():
    result = Checks(str(fail04_dir))
    problems = result.missing_employees()
    assert len(problems) == 0