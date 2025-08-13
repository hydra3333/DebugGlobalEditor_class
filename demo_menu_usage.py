
# demo_menu_usage.py
# Example 2: Add a menu item and listen for the applied event to refresh UI.

import tkinter as tk
from DebugGlobalEditor_class import DebugGlobalEditor_class

TITLE = "Menu Demo"
SCALE = 1.2
ENABLED = True
TOTAL = SCALE * (1 + int(ENABLED))

label = None

def refresh_ui(root):
    global label
    if label is None:
        label = tk.Label(root)
        label.pack(pady=8)
    label.config(text=f"{TITLE} | SCALE={SCALE} | ENABLED={ENABLED} | TOTAL={TOTAL}")

def open_editor(root):
    editor = DebugGlobalEditor_class(root, allow_recompute=True)
    result = editor.open()
    # Optional: result['changes'] to inspect what changed
    refresh_ui(root)

def main():
    root = tk.Tk()
    root.title(TITLE)
    refresh_ui(root)

    if __debug__:
        menubar = tk.Menu(root)
        debugmenu = tk.Menu(menubar, tearoff=0)
        debugmenu.add_command(label="Open Debug Globals", command=lambda: open_editor(root))
        menubar.add_cascade(label="Debug", menu=debugmenu)
        root.config(menu=menubar)

    # Also listen for virtual event (alternative to direct call)
    def on_applied(event=None):
        refresh_ui(root)
    root.bind("<<DebugGlobalsApplied>>", on_applied)

    root.mainloop()

if __name__ == "__main__":
    main()
