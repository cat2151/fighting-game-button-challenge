# Theme Mode Comparison

## Quick Reference Table

| Feature | Light Mode | Dark Mode | System Mode |
|---------|-----------|-----------|-------------|
| **Background** | System default (light) | #2b2b2b (dark gray) | Auto-detected |
| **Text Color** | Black | White | Auto-detected |
| **Success Flash** | #00FF00 (green) | #00FF00 (green) | #00FF00 (green) |
| **Fail Flash** | red | #ff4444 (red) | Depends on OS |
| **Auto-detection** | No | No | Yes (Windows 10/11) |
| **Eye Strain** | Higher in dark rooms | Lower in dark rooms | Optimal |
| **Configuration** | `mode = "light"` | `mode = "dark"` | `mode = "system"` |

## Visual Comparison

### Light Mode
```
┌─────────────────────────────────────────┐
│  ボタンチャレンジ (Light Background)    │
│                                         │
│  mission : 右 + 弱  (Black Text)        │
│  右 + 弱                                │
│                                         │
│  score:5 fail:2 前回:8                  │
└─────────────────────────────────────────┘
```

**Pros:**
- Familiar system default appearance
- Good for bright environments
- Traditional look

**Cons:**
- Can cause eye strain in dark rooms
- Higher screen brightness needed

### Dark Mode
```
┌─────────────────────────────────────────┐
█  ボタンチャレンジ (Dark Background)     █
█                                         █
█  mission : 右 + 弱  (White Text)        █
█  右 + 弱                                █
█                                         █
█  score:5 fail:2 前回:8                  █
└─────────────────────────────────────────┘
```

**Pros:**
- Reduces eye strain in dark environments
- Lower screen brightness needed
- Modern appearance
- Better for OLED screens (power saving)

**Cons:**
- May be too dark in bright environments
- Some users prefer light backgrounds

### System Mode
```
┌─────────────────────────────────────────┐
│ Auto-switches between Light and Dark    │
│ based on Windows OS settings            │
│                                         │
│ Windows Light Theme → Light Mode        │
│ Windows Dark Theme  → Dark Mode         │
│                                         │
│ Best of both worlds!                    │
└─────────────────────────────────────────┘
```

**Pros:**
- Automatically adapts to user preference
- Respects system-wide theme
- No manual switching needed
- Optimal for all lighting conditions

**Cons:**
- Only works on Windows 10/11
- Requires OS dark mode to be configured

## When to Use Each Mode

### Use Light Mode When:
- You prefer traditional light interfaces
- Working in bright environments
- Your OS doesn't support dark mode
- You have specific accessibility needs for high contrast on light backgrounds

### Use Dark Mode When:
- You work in dark or dim environments
- You want to reduce eye strain
- You prefer modern dark interfaces
- You want to save battery on OLED displays

### Use System Mode When:
- You want the app to match your OS theme
- You switch between bright and dark environments
- You're on Windows 10/11
- **This is the recommended default!**

## Flash Colors Comparison

### Success Flash (Mission Complete)

**Light Mode:**
- Background flashes to bright green (#00FF00)
- High visibility on light background

**Dark Mode:**
- Background flashes to bright green (#00FF00)
- Same color but appears brighter on dark background

### Fail Flash (Mission Failed)

**Light Mode:**
- Background flashes to red
- Standard red warning color

**Dark Mode:**
- Background flashes to #ff4444 (slightly lighter red)
- Better visibility on dark background

## Performance Notes

All theme modes have identical performance:
- No performance difference between modes
- Theme is applied at startup
- Hot reload supported for all modes
- 60 FPS maintained regardless of theme

## Customization Level

| Mode | Customization | Effort |
|------|---------------|--------|
| Light (default colors) | Low | None - just set mode |
| Dark (default colors) | Low | None - just set mode |
| System (default colors) | Low | None - just set mode |
| Custom Light | High | Edit 4 color values |
| Custom Dark | High | Edit 4 color values |
| Custom Both | Highest | Edit 8 color values |

## Migration from Old Version

If you're upgrading from a version without dark mode:

**Before:**
```toml
# No theme settings
title = "ボタンチャレンジ"
```

**After (automatic):**
```toml
# Theme is added automatically with defaults
[theme]
    mode = "system"
```

No changes needed! The default configuration works with both old and new versions.

## Troubleshooting

### System Mode Not Working?
- Check if you're on Windows 10/11
- Verify Windows dark mode is enabled in Settings → Personalization → Colors
- Restart the application after changing OS theme

### Colors Look Wrong?
- Check your TOML syntax is correct
- Verify color format (use # for hex colors)
- Try resetting to default by removing custom color definitions

### Want Different Colors?
- Copy the default theme section from `config/button_challenge.toml`
- Modify only the colors you want to change
- Save and use hot reload to see changes immediately
