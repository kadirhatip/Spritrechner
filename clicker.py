import PySimpleGUI as sg
# Um die Unschärfe rauszunehmen
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

title = "Clicker"

output = 0

layout = [
    [sg.Text(output, key = "_counter")],
    [sg.Button("Click", key = "_button-clicker")]
]

window = sg.Window(title, layout, size = (400, 400))

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "_button-clicker":
        output = output + 1
        window["_counter"].update(output)

    else: 
        print("Unexpected error")