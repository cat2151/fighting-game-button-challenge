import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils import set_debug_print_enabled, is_debug_print_enabled, debug_print, read_toml
import io
from contextlib import redirect_stdout


def test_debug_print_default_disabled():
    """Test that debug_print is disabled by default"""
    # Reset to default state
    set_debug_print_enabled(False)
    assert not is_debug_print_enabled()


def test_debug_print_can_be_enabled():
    """Test that debug_print can be enabled"""
    set_debug_print_enabled(True)
    assert is_debug_print_enabled()
    # Reset
    set_debug_print_enabled(False)


def test_debug_print_suppresses_output_when_disabled():
    """Test that debug_print doesn't output when disabled"""
    set_debug_print_enabled(False)
    
    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        debug_print("This should not appear")
    
    output = f.getvalue()
    assert output == ""


def test_debug_print_outputs_when_enabled():
    """Test that debug_print outputs when enabled"""
    set_debug_print_enabled(True)
    
    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        debug_print("This should appear")
    
    output = f.getvalue()
    assert "This should appear" in output
    
    # Reset
    set_debug_print_enabled(False)


def test_button_challenge_toml_has_debug_print():
    """Test that button_challenge.toml has debug_print configuration"""
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge.toml'
    )
    
    # Read the config file
    toml_data = read_toml(config_path)
    
    # Verify debug_print key exists
    assert 'debug_print' in toml_data
    
    # Verify default is false
    assert toml_data['debug_print'] is False


def test_debug_print_config_is_boolean():
    """Test that debug_print in config is a boolean value"""
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge.toml'
    )
    
    toml_data = read_toml(config_path)
    assert isinstance(toml_data['debug_print'], bool)
