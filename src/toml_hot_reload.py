"""
TOML hot reload functionality.
Tracks modification times of TOML files and detects changes.
"""
import os
from typing import Dict, List, Optional


class TomlFileTracker:
    """Tracks modification times of TOML files for hot reload detection."""
    
    def __init__(self):
        """Initialize the tracker with empty state."""
        self.file_mtimes: Dict[str, float] = {}
    
    def track_files(self, file_paths: List[str]) -> None:
        """
        Start tracking the specified TOML files.
        
        Args:
            file_paths: List of TOML file paths to track
        """
        self.file_mtimes = {}
        for path in file_paths:
            if path and os.path.exists(path):
                self.file_mtimes[path] = os.path.getmtime(path)
    
    def check_for_changes(self) -> bool:
        """
        Check if any tracked files have been modified.
        
        Returns:
            True if any file has been modified, False otherwise
        """
        for path, old_mtime in self.file_mtimes.items():
            if not os.path.exists(path):
                # File was deleted - consider this a change
                return True
            
            current_mtime = os.path.getmtime(path)
            if current_mtime != old_mtime:
                return True
        
        return False
    
    def update_mtimes(self) -> None:
        """Update the stored modification times after a reload."""
        for path in list(self.file_mtimes.keys()):
            if os.path.exists(path):
                self.file_mtimes[path] = os.path.getmtime(path)


def get_tracked_toml_files(args) -> List[str]:
    """
    Get list of TOML files to track based on args.
    
    Args:
        args: Configuration arguments object
    
    Returns:
        List of TOML file paths
    """
    files = []
    
    # Main config files
    if hasattr(args, 'config_filename') and args.config_filename:
        files.append(args.config_filename)
    
    if hasattr(args, 'mission_toml') and args.mission_toml:
        files.append(args.mission_toml)
    
    if hasattr(args, 'button_names_toml') and args.button_names_toml:
        files.append(args.button_names_toml)
    
    if hasattr(args, 'lever_toml') and args.lever_toml:
        files.append(args.lever_toml)
    
    if hasattr(args, 'alias_toml') and args.alias_toml:
        files.append(args.alias_toml)
    
    if hasattr(args, 'moves_toml') and args.moves_toml:
        files.append(args.moves_toml)
    
    return files
