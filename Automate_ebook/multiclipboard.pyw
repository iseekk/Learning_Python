#! python3
# multiclipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe multiclipboard.pyw save <keyword> - Saves clipboard to keyword.
# py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard.
# py.exe multiclipboard.pyw list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys


with shelve.open("mcb") as mcb_shelf:
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == "save":
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == "delete":
            if sys.argv[2]:
                del mcb_shelf[sys.argv[2]]
            else:
                for key in mcb_shelf.keys():
                    del mcb_shelf[key]

    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "list":
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
