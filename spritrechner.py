import PySimpleGUI as sg
# Um die Unschärfe rauszunehmen
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

title = "Converter"

layout = [
    [sg.InputText(key = "_input"), sg.Spin(["km to mile", "kg to pound", "sec to min"], key= "_spin"), sg.Button("Convert", key = "_button")],
    [sg.Text("Output", key = "_output")]
]

def get_factor(string):
    match string:
            case "km to mile":
                return 0.621
            case "kg to pound":
                return 2.205
            case "sec to min":
                return 1/60
            

window = sg.Window(title, layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "_button":
        input = values["_input"]
        spin = values["_spin"]

        factor = get_factor(spin)

        if input.isnumeric():
            solution_long = int(input) * factor
            # Formatiert das anzuzeigende Ergebnis mit zwei Dezimalstellen
            solution = "{:.2f}".format(solution_long)
            window["_output"].update(solution)
        else:
            window["_output"].update("Not a number!")