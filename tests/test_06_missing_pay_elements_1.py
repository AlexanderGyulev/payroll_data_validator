from validations import Checks
from pathlib import Path

data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail06_dir = data_dir / "fail_06_missing_pay_elements_1"

def test_missing_pay_elements_1_pass():
    result = Checks(str(pass_all_dir))
    problems = result.missing_pay_elements_1()
    assert len(problems) == 0

def test_missing_pay_elements_1_fail():
    result = Checks(str(fail06_dir))
    problems = result.missing_pay_elements_1()
    assert len(problems) == 0