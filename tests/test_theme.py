"""
Tests for theme module functionality.
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from theme import get_theme_colors, get_windows_dark_mode


def test_get_theme_colors_light_mode():
    """Test light mode returns light colors"""
    colors = get_theme_colors("light")
    assert colors is not None
    assert 'bg_color' in colors
    assert 'fg_color' in colors
    assert 'success_color' in colors
    assert 'fail_color' in colors


def test_get_theme_colors_dark_mode():
    """Test dark mode returns dark colors"""
    colors = get_theme_colors("dark")
    assert colors is not None
    assert 'bg_color' in colors
    assert colors['bg_color'] == '#2b2b2b'
    assert colors['fg_color'] == '#ffffff'


def test_get_theme_colors_system_mode():
    """Test system mode returns appropriate colors"""
    colors = get_theme_colors("system")
    assert colors is not None
    assert 'bg_color' in colors
    assert 'fg_color' in colors
    # Should return either light or dark colors


def test_get_theme_colors_with_custom_colors():
    """Test custom colors override defaults"""
    custom_light = {
        'bg_color': '#ffffff',
        'fg_color': '#000000',
        'success_color': '#00ff00',
        'fail_color': '#ff0000'
    }
    custom_dark = {
        'bg_color': '#000000',
        'fg_color': '#ffffff',
        'success_color': '#00ff00',
        'fail_color': '#ff0000'
    }
    
    light_colors = get_theme_colors("light", custom_light, custom_dark)
    assert light_colors['bg_color'] == '#ffffff'
    
    dark_colors = get_theme_colors("dark", custom_light, custom_dark)
    assert dark_colors['bg_color'] == '#000000'


def test_get_theme_colors_invalid_mode():
    """Test invalid mode defaults to light"""
    colors = get_theme_colors("invalid_mode")
    assert colors is not None
    # Should fall back to light mode
    assert colors['fg_color'] == 'black'


def test_get_windows_dark_mode():
    """Test Windows dark mode detection doesn't crash"""
    # This should not raise an exception
    result = get_windows_dark_mode()
    assert isinstance(result, bool)
