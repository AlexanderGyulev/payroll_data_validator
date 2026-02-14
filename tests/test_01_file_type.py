from validations import Checks
from pathlib import Path


data_dir = Path(__file__).resolve().parent / "data"

pass_all_dir = data_dir / "pass_all_tests"
fail01_dir = data_dir / "fail_01_file_type"

def test_file_type_pass():
    result = Checks(str(pass_all_dir))
    problems = result.check_file_type()
    assert len(problems) == 0

def test_file_type_fail():
    result = Checks(str(fail01_dir))
    problems = result.check_file_type()
    assert len(problems) == 0
