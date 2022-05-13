import tkinter as tk

breite = 600
höhe = 400
rand_oben = 50
rand_seite = 50
seitenmaße = f"{breite}x{höhe}+{rand_oben}+{rand_seite}"

fenster = tk.Tk()
fenster.title("Spritrechner")
fenster.geometry(seitenmaße)

aufforderung_lbl = tk.Label(fenster, text="Gib deinen Namen ein: ")
aufforderung_lbl.pack()

eingabe_entry = tk.Entry(fenster)
eingabe_entry.pack()

def ausgabe():
    name = str(eingabe_entry.getvar())
    print(name)





#Um die GUI scharfzustellen und sie dann zu starten
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    fenster.mainloop()