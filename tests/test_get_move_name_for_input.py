import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import get_move_name_for_input

@pytest.mark.parametrize(
    "input_str, moves, plus, expected",
    [
        # Exact match
        ("右 + 強 + 必", [{"name": "SA2", "input": "右 + 強 + 必"}], " + ", "SA2"),
        # Match with different order (should match due to formatting)
        ("必 + 強 + 右", [{"name": "SA2", "input": "右 + 強 + 必"}], " + ", "SA2"),
        # No match
        ("右 + 弱", [{"name": "SA2", "input": "右 + 強 + 必"}], " + ", ""),
        # Multiple moves, find correct one
        (
            "強 + 必",
            [
                {"name": "SA1", "input": "強 + 必"},
                {"name": "SA2", "input": "右 + 強 + 必"}
            ],
            " + ",
            "SA1"
        ),
        # Left direction SA2
        ("左 + 強 + 必", [{"name": "SA2", "input": "左 + 強 + 必"}], " + ", "SA2"),
        # Empty moves list
        ("右 + 強 + 必", [], " + ", ""),
        # No matching move
        (
            "下 + 弱",
            [
                {"name": "SA1", "input": "強 + 必"},
                {"name": "SA2", "input": "右 + 強 + 必"}
            ],
            " + ",
            ""
        ),
        # Extra whitespace handling
        (" 右 +  強  + 必 ", [{"name": "SA2", "input": "右 + 強 + 必"}], " + ", "SA2"),
    ]
)
def test_get_move_name_for_input(input_str, moves, plus, expected):
    result = get_move_name_for_input(input_str, moves, plus)
    assert result == expected
