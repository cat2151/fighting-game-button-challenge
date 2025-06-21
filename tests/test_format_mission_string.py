import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import format_mission_string

@pytest.mark.parametrize("mission, plus, expected", [
    ("右 + 強 + 必", " + ", " + ".join(sorted(["右", "強", "必"]))),
    ("必 + 強 + 右", " + ", " + ".join(sorted(["必", "強", "右"]))),
    ("上 + 弱", " + ", " + ".join(sorted(["上", "弱"]))),
    # 以下は運用上はありえないケース、仕様を明示するためのケース
    ("左", " + ", "左"),
    (" 右 +  強  + 必 ", " + ", " + ".join(sorted(["右", "強", "必"]))),
    ("A + B + C", " + ", " + ".join(sorted(["A", "B", "C"]))),
    ("C+B+A", " + ", "C+B+A"),  # 区切りが違う場合はそのまま
    ("", " + ", ""),
])
def test_format_mission_string(mission, plus, expected):
    assert format_mission_string(mission, plus) == expected
