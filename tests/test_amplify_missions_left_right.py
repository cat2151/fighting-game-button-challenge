import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from missions import amplify_missions_left_right


@pytest.mark.parametrize(
    "missions, left_right, left_right_temp, expected",
    [
        # 左右反転が発生する場合
        ([{"input": "右上"}], ["右", "左"], ["みぎ", "ひだり"], [
            {"input": "右上"}, {"input": "左上"}
        ]),
        # すでに左右反転済みのものが含まれる場合
        ([{"input": "右上"}, {"input": "左上"}], ["右", "左"], ["みぎ", "ひだり"], [
            {"input": "右上"}, {"input": "左上"}
        ]),
        # 反転しても同じ文字列の場合
        ([{"input": "上"}, {"input": "下"}], ["右", "左"], ["みぎ", "ひだり"], [
            {"input": "上"}, {"input": "下"}
        ]),
        # 複数ミッション
        ([{"input": "右 + 強"}, {"input": "左 + 弱"}], ["右", "左"], ["みぎ", "ひだり"], [
            {"input": "右 + 強"}, {"input": "左 + 弱"}, {"input": "左 + 強"}, {"input": "右 + 弱"}
        ]),
    ]
)
def test_amplify_missions_left_right(missions, left_right, left_right_temp, expected):
    result = amplify_missions_left_right(missions, left_right, left_right_temp)
    result_inputs = sorted([m["input"] for m in result])
    expected_inputs = sorted([m["input"] for m in expected])
    assert result_inputs == expected_inputs
