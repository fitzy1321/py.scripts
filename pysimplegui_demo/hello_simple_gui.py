import PySimpleGUI as sg

# Create GUI Elements
layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("Ok")]
]

# Create the window
window = sg.Window("Hello World", layout)

# Create the Event Loop
while True:
    event, values = window.read()

    if event == "Ok" or event == sg.WIN_CLOSED:
        break;

window.close()
