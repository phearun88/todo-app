import function
import FreeSimpleGUI
import FreeSimpleGUI as sg

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = FreeSimpleGUI.Window('My To-Do App', layout=[[label],[input_box, add_button] ])
window.read()
window.close()