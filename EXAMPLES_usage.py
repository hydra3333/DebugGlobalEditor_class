#-----------------------------------------------------------------------------------------------

# ... build your Tk app
if __debug__:
    tk.Button(root, text="Debug Globals", command=lambda: DebugGlobalEditor_class(root).open()).pack()
#-----------------------------------------------------------------------------------------------


# Practical pattern (safe and GC-friendly):
def open_DebugGlobalEditor_class():
    # No retained reference → collectible after close
   # DebugGlobalEditor(root).open()
    editor = DebugGlobalEditor(root)
    result = editor.open()
    #.. do something with the result, in whatever form the returned result is
   del editor  # optional; not required, but explicit if you want
   return