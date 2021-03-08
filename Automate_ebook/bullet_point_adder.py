#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

from pyperclip import copy, paste

text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

print("\n".join("* {t}".format(t=i) for i in text.split("\n")))
