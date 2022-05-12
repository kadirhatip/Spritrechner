import tkinter as tk

window = tk.Tk()

greeting_lbl = tk.Label(window, text="Hallo Welt")
greeting_lbl.pack()



#Um die GUI scharfzustellen und sie dann zu starten
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    window.mainloop()