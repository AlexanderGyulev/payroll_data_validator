from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail08_dir = data_dir / "fail_08_are_pay_elements_numeric"

def test_are_pay_elements_numeric_pass():
    result = Checks(str(pass_all_dir))
    problems = result.are_pay_elements_numeric()
    assert len(problems) == 0

def test_are_pay_elements_numeric_fail():
    result = Checks(str(fail08_dir))
    problems = result.are_pay_elements_numeric()
    assert len(problems) == 0