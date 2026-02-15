from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail07_dir = data_dir / "fail_07_missing_pay_elements_2"

def test_missing_pay_elements_2_pass():
    result = Checks(str(pass_all_dir))
    problems = result.missing_pay_elements_2()
    assert len(problems) == 0

def test_missing_pay_elements_2_fail():
    result = Checks(str(fail07_dir))
    problems = result.missing_pay_elements_2()
    assert len(problems) == 0