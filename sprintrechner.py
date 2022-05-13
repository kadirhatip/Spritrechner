import tkinter as tk

width = 600
height = 400
margin_top = 50
margin_side = 50
seitenmaße = f"{width}x{height}+{margin_top}+{margin_side}"

window = tk.Tk()
window.title("Spritrechner")
window.geometry(seitenmaße)

greeting_lbl = tk.Label(window, text="Hallo Welt")
greeting_lbl.pack()




#Um die GUI scharfzustellen und sie dann zu starten
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    window.mainloop()