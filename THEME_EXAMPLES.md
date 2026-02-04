# Dark Mode Configuration Examples

This file contains example configurations for different theme scenarios.

## Example 1: System Mode (Default - Recommended)

```toml
[theme]
    mode = "system"  # Automatically follows Windows OS dark mode setting
```

When using system mode, the application will:
- Detect Windows dark mode from registry
- Use dark theme when OS is in dark mode
- Use light theme when OS is in light mode
- Fall back to light theme on non-Windows systems

## Example 2: Always Dark Mode

```toml
[theme]
    mode = "dark"
```

Force dark mode regardless of OS settings. Uses default dark colors:
- Background: #2b2b2b (dark gray)
- Foreground: #ffffff (white)
- Success: #00FF00 (green)
- Fail: #ff4444 (red)

## Example 3: Always Light Mode

```toml
[theme]
    mode = "light"
```

Force light mode regardless of OS settings. Uses default light colors:
- Background: SystemButtonFace (system default)
- Foreground: black
- Success: #00FF00 (green)
- Fail: red

## Example 4: Custom Dark Theme

```toml
[theme]
    mode = "dark"
    
    [theme.dark]
        bg_color = "#1e1e1e"       # VS Code dark background
        fg_color = "#d4d4d4"       # Light gray text
        success_color = "#4ec9b0"  # Cyan success
        fail_color = "#f48771"     # Salmon red fail
```

## Example 5: Custom Light Theme

```toml
[theme]
    mode = "light"
    
    [theme.light]
        bg_color = "#f5f5f5"       # Light gray background
        fg_color = "#333333"       # Dark gray text
        success_color = "#00aa00"  # Darker green success
        fail_color = "#cc0000"     # Dark red fail
```

## Example 6: Custom Both Themes with System Detection

```toml
[theme]
    mode = "system"
    
    # Custom light theme
    [theme.light]
        bg_color = "#ffffff"
        fg_color = "#000000"
        success_color = "#00ff00"
        fail_color = "#ff0000"
    
    # Custom dark theme
    [theme.dark]
        bg_color = "#1a1a1a"
        fg_color = "#e0e0e0"
        success_color = "#00ff88"
        fail_color = "#ff6666"
```

## Example 7: High Contrast Dark Theme

```toml
[theme]
    mode = "dark"
    
    [theme.dark]
        bg_color = "#000000"       # Pure black
        fg_color = "#ffffff"       # Pure white
        success_color = "#00ff00"  # Bright green
        fail_color = "#ff0000"     # Bright red
```

## Example 8: Solarized Dark Theme

```toml
[theme]
    mode = "dark"
    
    [theme.dark]
        bg_color = "#002b36"       # Solarized dark base
        fg_color = "#839496"       # Solarized light text
        success_color = "#859900"  # Solarized green
        fail_color = "#dc322f"     # Solarized red
```

## Color Format

Colors can be specified in multiple formats:
- Hex format: `"#2b2b2b"`, `"#ffffff"`
- Named colors: `"black"`, `"white"`, `"red"`, `"green"`
- System colors: `"SystemButtonFace"` (Windows system default)

## Testing Your Configuration

1. Edit `config/button_challenge.toml`
2. Add your theme configuration
3. Run the application: `button_challenge.bat`
4. The theme will be applied immediately
5. You can also use hot reload to test changes without restarting

## Color Picker Tools

To find the perfect colors:
- Windows: Use the built-in Color Picker (PowerToys)
- Online: colorpicker.me, color.adobe.com
- VS Code: Built-in color picker in settings

## Accessibility Tips

For better accessibility:
- Ensure sufficient contrast between background and foreground (WCAG 2.1 Level AA requires 4.5:1)
- Test with actual use cases
- Consider users with color blindness
- Use system mode to respect user's OS preferences
