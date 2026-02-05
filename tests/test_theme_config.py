"""
Test that theme configuration is loaded properly from TOML
"""
import sys
import os
import argparse

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from configs import apply_theme_configuration


def test_apply_theme_configuration_with_theme_config():
    """Test applying theme configuration with full theme config"""
    args = argparse.Namespace()
    args.theme = {
        'mode': 'dark',
        'light': {
            'bg_color': '#ffffff',
            'fg_color': '#000000',
            'success_color': '#00ff00',
            'fail_color': '#ff0000'
        },
        'dark': {
            'bg_color': '#000000',
            'fg_color': '#ffffff',
            'success_color': '#00ff00',
            'fail_color': '#ff0000'
        }
    }
    
    args = apply_theme_configuration(args)
    
    assert hasattr(args, 'theme_colors')
    assert args.theme_colors['bg_color'] == '#000000'
    assert args.theme_colors['fg_color'] == '#ffffff'


def test_apply_theme_configuration_light_mode():
    """Test applying light theme configuration"""
    args = argparse.Namespace()
    args.theme = {
        'mode': 'light',
        'light': {
            'bg_color': 'white',
            'fg_color': 'black',
            'success_color': '#00ff00',
            'fail_color': 'red'
        }
    }
    
    args = apply_theme_configuration(args)
    
    assert hasattr(args, 'theme_colors')
    assert args.theme_colors['bg_color'] == 'white'
    assert args.theme_colors['fg_color'] == 'black'


def test_apply_theme_configuration_no_theme():
    """Test applying theme configuration when no theme is defined"""
    args = argparse.Namespace()
    
    args = apply_theme_configuration(args)
    
    # Should get default system theme (which may resolve to light or dark based on OS)
    assert hasattr(args, 'theme_colors')
    assert 'bg_color' in args.theme_colors
    assert 'fg_color' in args.theme_colors


def test_apply_theme_configuration_system_mode():
    """Test applying system theme configuration"""
    args = argparse.Namespace()
    args.theme = {
        'mode': 'system'
    }
    
    args = apply_theme_configuration(args)
    
    # Should get colors based on system settings (default to light on non-Windows)
    assert hasattr(args, 'theme_colors')
    assert 'bg_color' in args.theme_colors
    assert 'fg_color' in args.theme_colors
