import glob
import re

user_regex = re.compile(input("Enter regex: "))
file_names = glob.glob("*.txt")
rep = []

for name in file_names:
    with open(name, "r") as file:
        lines_list = file.readlines()
    [rep.append(match) for match in lines_list if user_regex.search(match)]


print("".join(_ for _ in rep))