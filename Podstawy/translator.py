geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404: nie znaleziono "
               "strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących "
                    "jakiejś osoby.",
        "Keyboard Plaque": "(skojarzone z kamieniem nazębnym)zanieczyszczenia "
                           "nagromadzone w klawiaturze komputera.",
        "Link Rot": "(obumieranie linków) proces, w wyniku którego linki do stron WWW "
                    "stają się nieaktualne.",
        "Percussive Maintenance": "(konserwacja perkusyjna)naprawa urządzenia "
                                  "elektronicznego przez stuknięcie.",
        "Uninstalled": "(odinstalowany) zwolniony z pracy; termin szczególnie popularny "
                       "w okresie bańki internetowej."
        }

choice = None

while choice != "0":
    print(
        """
    ==========
    Translator
    ==========
    0 - zakończ
    1 - znajdź termin
    2 - dodaj nowy termin
    3 - zmień definicję terminu
    4 - usuń termin
    """
    )

    choice = input("Wybierasz:")

    if choice == "0":
        print("Nara!")

    elif choice == "1":
        term = input("Jaki termin mam ci wyjaśnić?")
        if term in geek:
            print(geek[term])
        else:
            print("Nie znaleziono takiego terminu.")

    elif choice == "2":
        term = input("Jaki termin mam dodać?")
        if term not in geek:
            definition = input("Podaj definicję tego terminu:")
            geek[term] = definition
            print("Termin {} został dodany.".format(term))
        else:
            print("Termin {} już istnieje.".format(term))

    elif choice == "3":
        term = input("Definicję jakiego terminu mam zmienić?")
        if term in geek:
            definition = input("Podaj nową definicję tego terminu:")
            geek[term] = definition
            print("Termin {} ma teraz nową definicję.".format(term))
        else:
            print("Termin {} nie istnieje.".format(term))

    elif choice == "4":
        term = input("Jaki termin mam usunąć?")
        if term in geek:
            del geek[term]
            print("Termin {} został usunięty.".format(term))
        else:
            print("Termin {} nie istnieje.".format(term))

    else:
        print("{} to nie jest prawidłowy wybór. Spróbuj ponownie!".format(choice))

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
