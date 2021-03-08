import sys, pickle


def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as c:
        print('Plik {name} nie istnieje.\n{error}'.format(name=file_name, error=c))
        input('Aby zakończyć program, naciśnij klawisz Enter..')
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    points = next_line(the_file)
    if points:
        points = int(points[0])
    return category, question, answers, correct, explanation, points


def welcome(title):
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")


def ask_name():
    while True:
        name = input('Podaj swoje imię:')
        if not name.isalpha():
            print("Dozwolone są tylko znaki alfabetu. Spróbuj ponownie.")
            continue
        else:
            break
    return name


def show_highest_scores():
    highest_scores = []
    all_scores = open('kwiz_scores.dat', 'rb')
    pickled_score = pickle.load(all_scores)
    while True:
        highest_scores.append(pickled_score)
        try:
            pickled_score = pickle.load(all_scores)
        except EOFError:
            break
    all_scores.close()
    highest_scores.sort(key=lambda krotka: krotka[1], reverse=True)
    print(highest_scores)
    best_5 = highest_scores[:5]
    print("\nNajlepsze wyniki\n")
    print("GRACZ\t\tWYNIK")
    for j in best_5:
        n, s = j
        print("{name}\t\t{score}".format(name=n, score=s))


def main():
    trivia_file = open_file('kwiz.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    name = ask_name()
    score = 0
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        print('Kategoria pytania:', category)
        print('Pytanie:', question)
        for i in range(4):
            print('\t{num}. {answ}'.format(num=i+1, answ=answers[i]))
        answer = input('Jaka jest Twoja odpowiedź?')
        if answer == correct:
            print('Zgadza się!', end=' ')
            score += points
        else:
            print('Zła odpowiedź!', end=' ')
        print(explanation)
        print('Wynik:', score)
        category, question, answers, correct, explanation, points = next_block(trivia_file)
    trivia_file.close()

    print('To było ostatnie pytanie.\nTwój końcowy wynik:', score)
    entry = (name, score)
    all_scores = open('kwiz_scores.dat', 'ab')
    pickle.dump(entry, all_scores)
    all_scores.close()
    show_highest_scores()


if __name__ == '__main__':
    main()
