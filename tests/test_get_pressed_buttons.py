import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from joystick import get_pressed_buttons

@pytest.mark.parametrize(
    "names, bitstring, plus, expected",
    [
        # 1つも押されていない
        (['A', 'B', 'C'], '000', ' + ', ''),
        # 1つだけ押されている
        (['A', 'B', 'C'], '100', ' + ', 'A'),
        (['A', 'B', 'C'], '010', ' + ', 'B'),
        (['A', 'B', 'C'], '001', ' + ', 'C'),
        # 複数押されている
        (['A', 'B', 'C'], '110', ' + ', 'A + B'),
        (['A', 'B', 'C'], '101', ' + ', 'A + C'),
        (['A', 'B', 'C'], '011', ' + ', 'B + C'),
        (['A', 'B', 'C'], '111', ' + ', 'A + B + C'),
        # namesに空文字が含まれる場合
        (['A', '', 'C'], '101', ' + ', 'A + C'),
        (['', '', 'C'], '001', ' + ', 'C'),
        (['', '', ''], '000', ' + ', ''),
        # bitstringがnamesより長い場合
        (['A', 'B'], '1101', ' + ', 'A + B'),
        # bitstringがnamesより短い場合（短い分は無視される）
        (['A', 'B', 'C'], '10', ' + ', 'A'),
        # 区切り文字を変更
        (['A', 'B', 'C'], '110', '-', 'A-B'),
    ]
)
def test_get_pressed_buttons(names, bitstring, plus, expected):
    assert get_pressed_buttons(names, bitstring, plus) == expected
