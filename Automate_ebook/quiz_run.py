import random
import json


SCORE = 0
REMATCH = True


def user_choice():
    response = None
    while response not in ("A", "B", "C", "D"):
        response = input("Twoja odpowiedź: ").upper()
    return response


with open("quiz_data.json", "r") as data_file:
    quiz_data = json.load(data_file)
with open("answers.json", "r") as answers_file:
    all_answers = json.load(answers_file)

while REMATCH:
    question = quiz_data.pop(random.choice(range(len(quiz_data))))
    state, capital = question["state"], question["capital"]

    last_deleted = all_answers.pop(all_answers.index(capital))
    random.shuffle(all_answers)
    four_answers = [capital] + all_answers[:3]
    all_answers.append(last_deleted)
    random.shuffle(four_answers)
    dic = dict(zip(["A", "B", "C", "D"], four_answers))

    print(f"Stolicą stanu {state} jest:")
    print("\n".join(f"{k}. {v}" for k, v in dic.items()))

    user_input = user_choice()

    if dic[user_input] == capital:
        print("Poprawna odpowiedź!")
        SCORE += 1
    else:
        print("Zła odpowiedź!")

    again = ""
    while again not in ("t", "n"):
        again = input('\nCzy chcesz zagrać ponownie? (t/n):').lower()
    if again == 'n':
        REMATCH = False


print(f"Wynik końcowy: {SCORE}")
input("Koniec programu. Wciśnij Enter aby zakończyć.")
