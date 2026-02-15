from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail03_dir = data_dir / "fail_03_headers_changed"

def test_headers_changed_pass():
    result = Checks(str(pass_all_dir))
    problems = result.check_headers_changed()
    assert problems == [], problems

def test_headers_changed_fail():
    result = Checks(str(fail03_dir))
    problems = result.check_headers_changed()
    assert problems == [], problems