import re

file_name = input("Enter file name: ")

try:
    with open(f'{file_name}.txt', "r") as f:
        text = f.readline()
except FileNotFoundError:
    print("Such file does not exist.")
else:
    words = re.compile(r'ADJECTIVE|NOUN|VERB').findall(text)
    for word in words:
        new_word = input(f'Enter an {word.lower()}: ')
        text = text.replace(word, new_word, 1)

    with open(f"new_{file_name}.txt", "w") as nf:
        nf.write(text)