import os
import sys
import pytest
import tempfile
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from toml_hot_reload import TomlFileTracker, get_tracked_toml_files


def test_toml_file_tracker_initialization():
    """Test that TomlFileTracker initializes correctly."""
    tracker = TomlFileTracker()
    assert tracker.file_mtimes == {}


def test_toml_file_tracker_track_files():
    """Test tracking TOML files."""
    tracker = TomlFileTracker()
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f1:
        f1.write('[test]\nvalue = 1\n')
        f1_path = f1.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f2:
        f2.write('[test]\nvalue = 2\n')
        f2_path = f2.name
    
    try:
        # Track files
        tracker.track_files([f1_path, f2_path])
        
        # Verify files are tracked
        assert f1_path in tracker.file_mtimes
        assert f2_path in tracker.file_mtimes
        assert len(tracker.file_mtimes) == 2
    finally:
        # Clean up
        os.unlink(f1_path)
        os.unlink(f2_path)


def test_toml_file_tracker_check_no_changes():
    """Test that check_for_changes returns False when files haven't changed."""
    tracker = TomlFileTracker()
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
        f.write('[test]\nvalue = 1\n')
        f_path = f.name
    
    try:
        # Track file
        tracker.track_files([f_path])
        
        # Check for changes immediately (should be False)
        assert tracker.check_for_changes() == False
    finally:
        # Clean up
        os.unlink(f_path)


def test_toml_file_tracker_detect_changes():
    """Test that check_for_changes detects file modifications."""
    tracker = TomlFileTracker()
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
        f.write('[test]\nvalue = 1\n')
        f_path = f.name
    
    try:
        # Track file
        tracker.track_files([f_path])
        
        # Wait a bit to ensure time difference
        time.sleep(0.01)
        
        # Modify file
        with open(f_path, 'w') as f:
            f.write('[test]\nvalue = 2\n')
        
        # Check for changes (should be True)
        assert tracker.check_for_changes() == True
        
        # Update mtimes
        tracker.update_mtimes()
        
        # Check again (should be False now)
        assert tracker.check_for_changes() == False
    finally:
        # Clean up
        os.unlink(f_path)


def test_toml_file_tracker_detect_deletion():
    """Test that check_for_changes detects file deletion."""
    tracker = TomlFileTracker()
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
        f.write('[test]\nvalue = 1\n')
        f_path = f.name
    
    try:
        # Track file
        tracker.track_files([f_path])
        
        # Delete file
        os.unlink(f_path)
        
        # Check for changes (should be True)
        assert tracker.check_for_changes() == True
    except:
        # Clean up in case of failure
        if os.path.exists(f_path):
            os.unlink(f_path)
        raise


def test_toml_file_tracker_ignores_nonexistent():
    """Test that tracker ignores non-existent files during initialization."""
    tracker = TomlFileTracker()
    
    # Track a file that doesn't exist
    nonexistent_path = "/tmp/nonexistent_file_12345.toml"
    tracker.track_files([nonexistent_path])
    
    # Should not be tracked
    assert nonexistent_path not in tracker.file_mtimes


def test_get_tracked_toml_files():
    """Test getting list of TOML files from args."""
    class MockArgs:
        def __init__(self):
            self.config_filename = "config/main.toml"
            self.mission_toml = "config/mission.toml"
            self.button_names_toml = "config/buttons.toml"
            self.lever_toml = "config/lever.toml"
            self.alias_toml = "config/alias.toml"
            self.moves_toml = "config/moves.toml"
    
    args = MockArgs()
    files = get_tracked_toml_files(args)
    
    assert len(files) == 6
    assert "config/main.toml" in files
    assert "config/mission.toml" in files
    assert "config/buttons.toml" in files
    assert "config/lever.toml" in files
    assert "config/alias.toml" in files
    assert "config/moves.toml" in files


def test_get_tracked_toml_files_missing_attributes():
    """Test getting list when some attributes are missing."""
    class MockArgs:
        def __init__(self):
            self.config_filename = "config/main.toml"
            self.mission_toml = "config/mission.toml"
            # Other attributes not set
    
    args = MockArgs()
    files = get_tracked_toml_files(args)
    
    assert len(files) == 2
    assert "config/main.toml" in files
    assert "config/mission.toml" in files


def test_get_tracked_toml_files_none_values():
    """Test getting list when some attributes are None."""
    class MockArgs:
        def __init__(self):
            self.config_filename = "config/main.toml"
            self.mission_toml = None
            self.button_names_toml = "config/buttons.toml"
    
    args = MockArgs()
    files = get_tracked_toml_files(args)
    
    # None values should be filtered out
    assert len(files) == 2
    assert "config/main.toml" in files
    assert "config/buttons.toml" in files
    assert None not in files
