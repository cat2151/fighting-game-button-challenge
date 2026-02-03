# TOML Hot Reload Feature

## Overview
The application now supports hot-reloading of TOML configuration files. When any tracked TOML file is modified, the application automatically detects the change, reloads the configuration, and restarts from Phase 1.

## Use Cases
- **Debug Display Toggle**: Change `debug_print` flag in `config/button_challenge.toml` to enable/disable debug output without restarting
- **Move Maintenance**: Edit moves in `config/moves_sf6lily.toml` or `config/moves.toml` and see changes immediately
- **Mission Updates**: Modify missions in `config/mission.toml` and test them right away
- **UI Adjustments**: Update display formats or other UI settings on the fly

## How It Works

### Tracked Files
The following TOML files are monitored for changes:
- `config/button_challenge.toml` - Main configuration
- `config/mission.toml` - Mission definitions
- `config/button_names.toml` - Button name mappings
- `config/lever_names.toml` - Lever/directional input names
- `config/alias.toml` - Display aliases
- `config/moves_sf6lily.toml` - Move definitions (if configured)

### Detection and Reload Process
1. **Monitoring**: The application checks for file modifications every 60 frames (approximately once per second at 60fps)
2. **Detection**: Modification times of all tracked files are compared to their previous values
3. **Reload**: When a change is detected:
   - All configuration files are reloaded
   - Game state is reset (score, fail count, etc.)
   - Challenge phase is reset to Phase 1
   - Mission index is reset to 0
   - User sees message: "=== TOML file changes detected, reloading configuration ==="

### Phase Reset Behavior
After hot reload, the game always:
- Restarts from **Phase 1** (button practice phase)
- Starts from the **first mission** (index 0)
- Resets all scores and statistics
- Preserves joystick and GUI window state

## Usage Example

1. Start the application normally
2. Edit any TOML file (e.g., change `debug_print = false` to `debug_print = true` in `config/button_challenge.toml`)
3. Save the file
4. Within ~1 second, the console will display:
   ```
   === TOML file changes detected, reloading configuration ===
   === Configuration reloaded, restarting from Phase 1 ===
   ```
5. Continue playing with the new configuration

## Technical Details

### Implementation
- **File Tracker**: `TomlFileTracker` class tracks modification times (`os.path.getmtime()`)
- **Check Interval**: 60 frames = ~1 second at 60fps
- **Reload Function**: `reload_configuration_and_reset()` handles safe reloading with error handling
- **State Reset**: Complete game state is reconstructed to Phase 1 starting conditions

### Error Handling
If an error occurs during reload (e.g., invalid TOML syntax):
- Error message is printed to console with full traceback
- Application continues running with previous configuration
- User can fix the TOML file and save again to retry

### Performance Impact
- Minimal: File modification check is lightweight (only reads file metadata)
- Check frequency: Once per second
- No performance impact during normal gameplay

## Testing
Run the test suite to verify hot reload functionality:
```bash
python -m pytest tests/test_toml_hot_reload.py -v
```

Run the manual test to see hot reload in action:
```bash
python tests/manual_test_hot_reload.py
```
