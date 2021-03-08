pairs = {"a1": "a2", "b1": "b2", "c1": "c2", "a2": "a3", "b2": "b3", "c2": "c3"}

choice = None

while choice != "0":
    print(
        """
    ====================
    Kto jest twoim tatą?
    ====================
    0 - zakończ
    1 - sprawdź kto jest tatą
    2 - dodaj
    3 - zmień
    4 - usuń
    5 - pokaż wszystkich
    6 - sprawdź kto jest dziadkiem
    """
    )

    choice = input("Wybierasz:")

    if choice == "0":
        print("Nara!")

    elif choice == "1":
        son = input("Podaj imię i nazwisko syna:")
        print("\n", pairs[son])
        input("\n nacisnij dowolny klawisz, aby kontynuować...")

    elif choice == "2":
        son = input("Podaj imię i nazwisko syna:")
        if son not in pairs:
            father = input("Podaj imię i nazwisko ojca:")
            pairs[son] = father
        else:
            print("Taka osoba już jest")
        input("\n nacisnij dowolny klawisz, aby kontynuować...")

    elif choice == "3":
        son = input("Podaj imię i nazwisko syna:")
        if son in pairs:
            father = input("Podaj nowe imię i nazwisko ojca dla {son}:".format(son=son))
            pairs[son] = father
        else:
            print("Nie ma takiej osoby")
        input("\n nacisnij dowolny klawisz, aby kontynuować...")

    elif choice == "4":
        son = input("Podaj imię i nazwisko syna, którego parę chcesz usunąć:")
        if son in pairs:
            del pairs[son]
        else:
            print("Nie ma takiej osoby")
        input("\n nacisnij dowolny klawisz, aby kontynuować...")

    elif choice == "5":
        print(pairs)
        input("\n nacisnij dowolny klawisz, aby kontynuować...")

    elif choice == "6":
        son = input("Podaj imię i nazwisko syna:")
        if son in pairs:
            father = pairs[son]
            if father in pairs:
                print("Dziadkiem {son} jest {grandpa}".format(son=son, grandpa=pairs[father]))
            else:
                print("Ta osoba nie ma dziadka")
        else:
                print("Nie ma takiej osoby")

        input("\n nacisnij dowolny klawisz, aby kontynuować...")
