import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # テスト対象関数を親ディレクトリからimportする用
from missions import is_no_count_case

no_count_names_list = [
    {"success": "右上", "no_count": ["右"]},
]

@pytest.mark.parametrize("mission_success, input_name, no_count_names_param, expect_exception, expected", [
    ("右上", "右上", no_count_names_list, False, True),
    ("右上", "右", no_count_names_list, False, True),
    ("右上", "上", no_count_names_list, False, False),
    ("右上", "右 + DP", no_count_names_list, False, False),
    ("右上", "右 + 必", no_count_names_list, False, False),
    ("右上", "ア + 必", no_count_names_list, False, False),
    ("右上", "左上", no_count_names_list, False, False),

    ("右", "右", no_count_names_list, False, True),
    ("右", "右上", no_count_names_list, False, False),
    ("右", "上", no_count_names_list, False, False),
    ("右", "右 + DP", no_count_names_list, False, False),
    ("右", "右 + 必", no_count_names_list, False, False),
    ("右", "ア + 必", no_count_names_list, False, False),
    ("右", "左上", no_count_names_list, False, False),

    ("上", "上", no_count_names_list, False, True),
    ("上", "右上", no_count_names_list, False, False),
    ("上", "上 + 弱", no_count_names_list, False, False),

    ("右 + 強 + 必", "右 + 強 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右", no_count_names_list, False, True),
    ("右 + 強 + 必", "強", no_count_names_list, False, True),
    ("右 + 強 + 必", "必", no_count_names_list, False, True),
    ("右 + 強 + 必", "強 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 強", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 強 + 必 + DP", no_count_names_list, False, False),
    ("右 + 強 + 必", "なし", no_count_names_list, False, False),

    # no_count_names_list が空のケースはExceptionを期待する
    ("上", "上", [], True, None),
    ("上", "右上", [], True, None),
])
def test_is_no_count_case(mission_success, input_name, no_count_names_param, expect_exception, expected):
    plus = " + "
    if expect_exception:
        with pytest.raises(ValueError):
            is_no_count_case(mission_success, input_name, no_count_names_param, plus)
    else:
        assert is_no_count_case(mission_success, input_name, no_count_names_param, plus) == expected
