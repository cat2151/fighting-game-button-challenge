import argparse
import toml

# Global variable to store debug_print flag
_debug_print_enabled = False

def set_debug_print_enabled(enabled):
    """Set the global debug_print flag"""
    global _debug_print_enabled
    _debug_print_enabled = enabled

def is_debug_print_enabled():
    """Check if debug printing is enabled"""
    return _debug_print_enabled

def debug_print(message):
    """Print debug message if debug_print is enabled"""
    if _debug_print_enabled:
        print(message)

def get_args():
    parser = argparse.ArgumentParser(description="Display an image for 1 second.")
    parser.add_argument("--config-filename", type=str, help="Path to the config file")
    args = parser.parse_args()
    return args

def update_args_by_toml(args, config_filename=None):
    if not config_filename:
        config_filename = args.config_filename
    debug_print(f'args : before: {args}')
    toml_data = read_toml(config_filename)
    debug_print(f'TOML : {toml_data}')
    for key, value in toml_data.items():
        setattr(args, key, value)
    debug_print(f'args : after : {args}')
    
    # Initialize debug_print global flag if present in config
    if hasattr(args, 'debug_print'):
        set_debug_print_enabled(args.debug_print)
    
    return args

def read_toml(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        toml_data = toml.load(f)
    return toml_data
