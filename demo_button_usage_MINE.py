
# ... build your Tk app
if __debug__:
    tk.Button(root, text="Debug Globals", command=lambda: DebugGlobalEditor_class(root).open()).pack()

