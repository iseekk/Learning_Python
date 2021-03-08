attributes = {"siła" : 0,
              "zdrowie" : 0,
              "mądrość" : 0,
              "zręczność" : 0
              }
points_left = 30
choice = None

while choice != "0":
    print(
        """
    ===============
    Kreator postaci
    ===============
    0 - zakończ
    1 - dodaj punkt do atrybutu
    2 - usuń punkt z atrybutu
    3 - pokaż atrybuty
    """
    )

    choice = input("Wybierasz:")

    if choice == "0":
        print("Nara!")

    elif choice == "1":
        attribute = input("Do jakiego atrybutu chcesz dodać puntky?")
        points = int(input("Ile puntków?"))
        if points < 0:
            print("\nNie możesz dodać takiej ilości punktów")
        elif points > points_left:
            print("\nNie masz tylu punktów")
        else:
            attributes[attribute] += points
            points_left -= points
            print("Do atrybutu {attribute} dodano {points} pkt.".format(attribute=attribute, points=points))

    elif choice == "2":
        attribute = input("Od jakiego atrybutu chcesz odjąć puntky?")
        points = int(input("Ile puntków?"))
        if points < 0:
            print("\nNie możesz odjąć takiej ilości punktów")
        elif points > attributes[attribute]:
            print("\nNie masz tylu punktów w tym atrybucie")
        else:
            attributes[attribute] -= points
            points_left += points
            print("Od atrybutu {attribute} odjęto {points} pkt.".format(attribute=attribute, points=points))

    elif choice == "3":
        print(attributes)
        print("Pozostałe punkty: {}".format(points_left))
