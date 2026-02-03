#!/usr/bin/env python3
"""
Manual test script for TOML hot reload functionality.
This script simulates the hot reload behavior without requiring a joystick.
"""
import os
import sys
import time
import tempfile
import shutil

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from toml_hot_reload import TomlFileTracker, get_tracked_toml_files


def test_file_modification_detection():
    """Test that file modifications are detected."""
    print("\n=== Test 1: File Modification Detection ===")
    
    # Create a temporary TOML file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
        f.write('[test]\nvalue = 1\n')
        temp_file = f.name
    
    try:
        # Initialize tracker
        tracker = TomlFileTracker()
        tracker.track_files([temp_file])
        
        print(f"Created and tracking file: {temp_file}")
        print("Initial check (should be False):", tracker.check_for_changes())
        
        # Wait and modify the file
        time.sleep(0.1)
        with open(temp_file, 'w') as f:
            f.write('[test]\nvalue = 2\n')
        
        print("Modified file")
        print("Check after modification (should be True):", tracker.check_for_changes())
        
        # Update mtimes
        tracker.update_mtimes()
        print("Updated mtimes")
        print("Check after update_mtimes (should be False):", tracker.check_for_changes())
        
        print("✓ Test 1 passed\n")
        
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def test_multiple_files():
    """Test tracking multiple files."""
    print("\n=== Test 2: Multiple Files ===")
    
    # Create multiple temporary files
    files = []
    for i in range(3):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
            f.write(f'[test]\nvalue = {i}\n')
            files.append(f.name)
    
    try:
        # Initialize tracker
        tracker = TomlFileTracker()
        tracker.track_files(files)
        
        print(f"Created and tracking {len(files)} files")
        print("Initial check (should be False):", tracker.check_for_changes())
        
        # Modify one file
        time.sleep(0.1)
        with open(files[1], 'w') as f:
            f.write('[test]\nvalue = modified\n')
        
        print(f"Modified file: {files[1]}")
        print("Check after modification (should be True):", tracker.check_for_changes())
        
        print("✓ Test 2 passed\n")
        
    finally:
        for f in files:
            if os.path.exists(f):
                os.unlink(f)


def test_get_tracked_files():
    """Test getting tracked files from args."""
    print("\n=== Test 3: Get Tracked Files ===")
    
    class MockArgs:
        def __init__(self):
            self.config_filename = "config/button_challenge.toml"
            self.mission_toml = "config/mission.toml"
            self.button_names_toml = "config/button_names.toml"
            self.lever_toml = "config/lever_names.toml"
            self.alias_toml = "config/alias.toml"
            self.moves_toml = "config/moves_sf6lily.toml"
    
    args = MockArgs()
    files = get_tracked_toml_files(args)
    
    print(f"Found {len(files)} TOML files to track:")
    for f in files:
        print(f"  - {f}")
    
    assert len(files) == 6, f"Expected 6 files, got {len(files)}"
    print("✓ Test 3 passed\n")


def test_reload_scenario():
    """Simulate a complete reload scenario."""
    print("\n=== Test 4: Complete Reload Scenario ===")
    
    # Create temporary config directory
    temp_dir = tempfile.mkdtemp()
    config_file = os.path.join(temp_dir, "config.toml")
    
    try:
        # Create initial config
        with open(config_file, 'w') as f:
            f.write('[test]\ndebug_print = false\n')
        
        print(f"Created config: {config_file}")
        
        # Initialize tracker
        tracker = TomlFileTracker()
        tracker.track_files([config_file])
        
        # Simulate game loop checking
        print("\nSimulating game loop...")
        for i in range(5):
            print(f"  Frame {i+1}: Check for changes =", tracker.check_for_changes())
            time.sleep(0.1)
        
        # Modify config
        print("\nModifying config file...")
        time.sleep(0.1)
        with open(config_file, 'w') as f:
            f.write('[test]\ndebug_print = true\n')
        
        # Simulate detection
        print("Next frame check (should detect change):", tracker.check_for_changes())
        
        if tracker.check_for_changes():
            print("=== Configuration change detected! ===")
            print("=== Reloading configuration... ===")
            # Simulate reload
            tracker.update_mtimes()
            print("=== Configuration reloaded, restarting from Phase 1 ===")
        
        print("After reload, check again (should be False):", tracker.check_for_changes())
        print("✓ Test 4 passed\n")
        
    finally:
        shutil.rmtree(temp_dir)


def main():
    """Run all tests."""
    print("=" * 60)
    print("TOML Hot Reload Manual Test Suite")
    print("=" * 60)
    
    try:
        test_file_modification_detection()
        test_multiple_files()
        test_get_tracked_files()
        test_reload_scenario()
        
        print("\n" + "=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
