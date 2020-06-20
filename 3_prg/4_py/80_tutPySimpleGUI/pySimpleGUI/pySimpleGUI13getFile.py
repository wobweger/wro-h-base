import PySimpleGUI as sg
import sys

sg.change_look_and_feel('Dark Grey 3')

fname = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Document to open')

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
