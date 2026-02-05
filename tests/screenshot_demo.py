#!/usr/bin/env python
"""
Screenshot demo script to show different theme modes.
Creates screenshots of each theme mode for documentation.
"""
import sys
import os
import tkinter as tk

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from theme import get_theme_colors


def create_demo_window(mode, colors):
    """Create a demo window resembling the actual application"""
    root = tk.Tk()
    root.title(f"ボタンチャレンジ - {mode.upper()} Mode Demo")
    root.geometry("700x150+100+100")
    root.config(bg=colors['bg_color'])
    
    # Create labels similar to the actual application
    labels = []
    
    # Label 1: Mission
    label1 = tk.Label(
        root, 
        text="mission : 右 + 弱",
        font=("Arial", 20),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    label1.pack()
    labels.append(label1)
    
    # Label 2: Current input
    label2 = tk.Label(
        root,
        text="右 + 弱",
        font=("Arial", 20),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    label2.pack()
    labels.append(label2)
    
    # Label 3: Empty
    label3 = tk.Label(
        root,
        text="",
        font=("Arial", 20),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    label3.pack()
    labels.append(label3)
    
    # Label 4: Score info
    label4 = tk.Label(
        root,
        text="score:5 fail:2 前回:8 最速:6 hist中心:7 now:0",
        font=("Arial", 20),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    label4.pack()
    labels.append(label4)
    
    return root, labels


def demo_success_flash(root, labels, colors):
    """Show success flash effect"""
    success_color = colors['success_color']
    
    # Flash success color
    root.config(bg=success_color)
    for label in labels:
        label.config(bg=success_color)
    
    root.update()


def demo_fail_flash(root, labels, colors):
    """Show fail flash effect"""
    fail_color = colors['fail_color']
    
    # Flash fail color
    root.config(bg=fail_color)
    for label in labels:
        label.config(bg=fail_color)
    
    root.update()


def main():
    """Create demo windows and show theme examples"""
    modes = {
        "light": "ライトモード",
        "dark": "ダークモード", 
        "system": "システム設定追従"
    }
    
    print("Theme Demo - Creating screenshots")
    print("=" * 50)
    
    for mode, mode_jp in modes.items():
        print(f"\n{mode_jp} ({mode}):")
        colors = get_theme_colors(mode)
        print(f"  Background: {colors['bg_color']}")
        print(f"  Foreground: {colors['fg_color']}")
        print(f"  Success:    {colors['success_color']}")
        print(f"  Fail:       {colors['fail_color']}")
    
    print("\n完了!")


if __name__ == "__main__":
    main()
