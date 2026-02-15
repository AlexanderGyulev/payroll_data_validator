from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail02_dir = data_dir / "fail_02_line_breaks"

def test_line_breaks_pass():
    result = Checks(str(pass_all_dir))
    problems = result.check_line_breaks()
    assert problems == [], problems

def test_line_breaks_fail():
    result = Checks(str(fail02_dir))
    problems = result.check_line_breaks()
    assert problems == [], problems