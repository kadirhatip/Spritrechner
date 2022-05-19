import PySimpleGUI as sg

title = "Mein erstes Fenster"

layout = [
    [sg.Text("Gib deinen Namen ein und drücke den Knopf")],
    [sg.InputText(key="_input"), sg.Button("Knopf", key="_knopf")],
    [sg.Text("Ausgabe", key="_ausgabe")]
]

window = sg.Window(title, layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "_knopf":
        window.find_element("_ausgabe").update(("Hallo %s" % values["_input"]))