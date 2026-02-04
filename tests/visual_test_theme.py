"""
Visual test script to demonstrate theme modes.
This creates a simple Tkinter window to show the different theme colors.
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from theme import get_theme_colors
import tkinter as tk


def create_theme_demo_window(mode, colors):
    """Create a demo window showing the theme colors"""
    root = tk.Tk()
    root.title(f"Theme Demo - {mode.upper()} Mode")
    root.geometry("400x300")
    root.config(bg=colors['bg_color'])
    
    # Title label
    title = tk.Label(
        root, 
        text=f"{mode.upper()} MODE",
        font=("Arial", 20, "bold"),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    title.pack(pady=20)
    
    # Sample text
    text1 = tk.Label(
        root,
        text="Background color: " + colors['bg_color'],
        font=("Arial", 12),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    text1.pack(pady=5)
    
    text2 = tk.Label(
        root,
        text="Foreground color: " + colors['fg_color'],
        font=("Arial", 12),
        bg=colors['bg_color'],
        fg=colors['fg_color']
    )
    text2.pack(pady=5)
    
    # Success color demo
    success_label = tk.Label(
        root,
        text="SUCCESS!",
        font=("Arial", 16, "bold"),
        bg=colors['success_color'],
        fg="black"
    )
    success_label.pack(pady=10)
    
    # Fail color demo
    fail_label = tk.Label(
        root,
        text="FAILED",
        font=("Arial", 16, "bold"),
        bg=colors['fail_color'],
        fg="white"
    )
    fail_label.pack(pady=10)
    
    # Close button
    close_btn = tk.Button(
        root,
        text="Close",
        command=root.destroy,
        font=("Arial", 12)
    )
    close_btn.pack(pady=20)
    
    return root


def main():
    """Show demo windows for all theme modes"""
    modes = ["light", "dark", "system"]
    
    print("Theme Demo")
    print("=" * 50)
    
    for mode in modes:
        colors = get_theme_colors(mode)
        print(f"\n{mode.upper()} MODE:")
        print(f"  Background: {colors['bg_color']}")
        print(f"  Foreground: {colors['fg_color']}")
        print(f"  Success:    {colors['success_color']}")
        print(f"  Fail:       {colors['fail_color']}")
        
        # Create and show demo window
        print(f"\nShowing {mode} mode window...")
        root = create_theme_demo_window(mode, colors)
        root.mainloop()
    
    print("\nDemo complete!")


if __name__ == "__main__":
    main()
