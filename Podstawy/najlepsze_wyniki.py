scores = [("Kamil", 100), ("Wojtek", 70), ("Tomek", 50), ("Ola", 85)]
choice = None

while choice != "0":
    print(
    """
    ========
      MENU
    ========
    0 - zakończ
    1 - pokaż wyniki
    2 - dodaj wynik
    3 - usuń wynik
    """
          )

    choice = input("Wybierasz:")

    if choice == "0":
        print("Nara!")
    elif choice == "1":
        print("\nNajlepsze wyniki\n")
        print("GRACZ\tWYNIK")
        for entry in scores:
            name, score = entry
            print("{name}\t{score}".format(name=name, score=score))
    elif choice == "2":
        name = input("Podaj imię gracza: ")
        score = int(input("Podaj wynik: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    elif choice == "3":
        name = input("Podaj imię gracza: ")
        index = scores.index(name)                  #???
        print(index)
        #entry = (name, score)
        #scores.append(entry)
        #scores.sort(reverse=True)
        #scores = scores[:5]
    else:
        print("'{}' to zły wybór!".format(choice))


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
