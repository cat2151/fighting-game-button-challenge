"""
Theme management for the application.
Supports light, dark, and system (auto) theme modes.
"""
import platform

def get_windows_dark_mode():
    """
    Windows OSのダークモード設定を取得する
    Get Windows OS dark mode setting
    
    Returns:
        bool: ダークモードが有効な場合True、それ以外はFalse
              True if dark mode is enabled, False otherwise
    """
    if platform.system() != "Windows":
        return False
    
    try:
        import winreg
        # Windows 10/11のPersonalization設定からAppsUseLightThemeを読み取る
        # 0 = ダークモード, 1 = ライトモード
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        )
        value, _ = winreg.QueryValueEx(registry_key, "AppsUseLightTheme")
        winreg.CloseKey(registry_key)
        return value == 0  # 0ならダークモード
    except Exception:
        # レジストリ読み取りに失敗した場合はライトモードとして扱う
        return False

def get_theme_colors(theme_mode, light_colors=None, dark_colors=None):
    """
    テーマモードに基づいて適切な色設定を返す
    Return appropriate color settings based on theme mode
    
    Args:
        theme_mode (str): "light", "dark", or "system"
        light_colors (dict): ライトモードの色設定 / Light mode color settings
        dark_colors (dict): ダークモードの色設定 / Dark mode color settings
    
    Returns:
        dict: 適用すべき色設定 / Color settings to apply
    """
    # デフォルトの色設定
    default_light = {
        'bg_color': 'SystemButtonFace',
        'fg_color': 'black',
        'success_color': '#00FF00',
        'fail_color': 'red'
    }
    
    default_dark = {
        'bg_color': '#2b2b2b',
        'fg_color': '#ffffff',
        'success_color': '#00FF00',
        'fail_color': '#ff4444'
    }
    
    # 引数で指定された色があればそれを使用、なければデフォルト
    light_colors = light_colors or default_light
    dark_colors = dark_colors or default_dark
    
    # テーマモードに応じて色を選択
    if theme_mode == "dark":
        return dark_colors
    elif theme_mode == "light":
        return light_colors
    elif theme_mode == "system":
        # システムのダークモード設定を確認
        is_dark = get_windows_dark_mode()
        return dark_colors if is_dark else light_colors
    else:
        # 不明なモードの場合はライトモードをデフォルトとする
        return light_colors
