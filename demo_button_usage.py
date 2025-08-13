
# demo_button_usage.py
# Example 1: Add a debug button that opens the editor before mainloop.

import tkinter as tk
from DebugGlobalEditor_class import DebugGlobalEditor_class

# Top-level simple globals
APP_TITLE = "Demo App"
MAX_ITEMS = 42
ALPHA = 0.8
DARK = False
ALPHA_PERCENT = int(ALPHA * 100)  # derived

def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    tk.Label(root, text=f"{APP_TITLE} (MAX_ITEMS={MAX_ITEMS}, ALPHA={ALPHA})").pack(pady=8)

    if __debug__:
        tk.Button(root, text="Debug Globals", command=lambda: DebugGlobalEditor_class(root).open()).pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    main()
