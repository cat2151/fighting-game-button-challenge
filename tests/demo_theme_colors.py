#!/usr/bin/env python
"""
Simple text demo to show theme colors for each mode.
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from theme import get_theme_colors


def print_theme_info(mode, colors):
    """Print theme information"""
    mode_names = {
        "light": "ライトモード (Light Mode)",
        "dark": "ダークモード (Dark Mode)",
        "system": "システム設定追従 (System Mode)"
    }
    
    print(f"\n{'=' * 60}")
    print(f"{mode_names.get(mode, mode.upper())}")
    print(f"{'=' * 60}")
    print(f"  背景色 (Background):  {colors['bg_color']}")
    print(f"  文字色 (Foreground):  {colors['fg_color']}")
    print(f"  成功色 (Success):     {colors['success_color']}")
    print(f"  失敗色 (Fail):        {colors['fail_color']}")
    print()


def main():
    """Show theme colors for all modes"""
    print("\n" + "=" * 60)
    print("ボタンチャレンジ - ダークモード設定デモ")
    print("Button Challenge - Dark Mode Settings Demo")
    print("=" * 60)
    
    modes = ["light", "dark", "system"]
    
    for mode in modes:
        colors = get_theme_colors(mode)
        print_theme_info(mode, colors)
    
    print("=" * 60)
    print("設定方法 (Configuration):")
    print("=" * 60)
    print("config/button_challenge.toml で以下のように設定:")
    print()
    print("[theme]")
    print('    mode = "light"   # ライトモード')
    print('    mode = "dark"    # ダークモード')
    print('    mode = "system"  # OSの設定に追従')
    print()
    print("カラーのカスタマイズも可能:")
    print()
    print("[theme.dark]")
    print('    bg_color = "#2b2b2b"')
    print('    fg_color = "#ffffff"')
    print('    success_color = "#00FF00"')
    print('    fail_color = "#ff4444"')
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
