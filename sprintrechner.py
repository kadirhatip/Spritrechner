import PySimpleGUI as sg
# Um die Unschärfe rauszunehmen
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

title = "Converter"

layout = [
    [sg.InputText(key = "_input"), sg.Spin(["km to mile", "kg to pound", "sec to min"], key= "_spin"), sg.Button("Convert", key = "_button")],
    [sg.Text("Output", key = "_output")]
]

window = sg.Window(title, layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "_button":
        input = window.find_element("_input").get()
        spin = window.find_element("_spin").get()

        if (spin == "km to mile"):
            factor = 0.621
        elif (spin == "kg to pound"):
            factor = 2.205
        elif (spin == "sec to min"):
            factor = 1/60
        
        solution = int(input) * factor
    
        window.find_element("_output").update(solution)