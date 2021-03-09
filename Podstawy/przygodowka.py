class Creature:

    def __init__(self, name, health_points=100, attack=10):
        self.name = name
        self.health_points = health_points
        self.attack = attack

    def __str__(self):
        return "{}: {}HP".format(self.name, self.health_points)

    def attack(self, target):
        target.health_points -= self.attack
        print("{} atakuje {} za {} pkt. życia".format(self.name, target.name, self.attack))


class Inventory:
    def __init__(self):
        self.items = []

    def __str__(self):
        message = ", ".join([i for i in self.items])
        return "W ekwipunku masz: {}".format(message, end=".")

    def add_item(self, item, other_inventory):
        self.items.append(item)
        other_inventory.items.remove(item)

    def remove_item(self, item):
        self.items.remove(item)


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Place:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.items = []

    @staticmethod
    def battle(one, two):
        while one.health_points <= 0 or two.health_points <= 0:
            one.attack(two)
            two.attack(one)
            print(one, end=", ")
            print(two)

    def enter_place(self, who):
        self.guests.append(who)
        print(who, "wchodzi do", self.name)

    def search(self):
        print("Widzisz przedmioty: {}".format(", ".join([str(a) for a in self.items]) if self.items else "brak"),
              end=".\n")
        print("Widzisz wrogów: {}".format(", ".join([a for a in self.guests]) if self.guests else "brak"), end=".")


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name=name)
        self.attack = attack


class HealthPotion(Item):
    def __init__(self, name, amount):
        super(HealthPotion, self).__init__(name=name)
        self.amount = amount

    def use_potion(self, who):
        who.health_points += self.amount


class Player(Creature):
    def __init__(self, name):
        super(Player, self).__init__(name=name)
        self.inventory = Inventory()
        self.weapon = None

    def equip_weapon(self, item):
        self.attack = item.attack


class Storage(Place):
    def __init__(self, name="Magazyn"):
        super(Storage, self).__init__(name=name)
        self.items.append(Weapon(name="Krótki miecz", attack=25))
        self.items.append(HealthPotion(name="Czerwona mikstura", amount=50))


class Sewers(Place):
    def __init__(self, name="Kanały"):
        super(Sewers, self).__init__(name=name)
        self.guests.append(Creature("Pająk", health_points=30, attack=15))


def ask_name():
    while True:
        name = input("Jak się nazywasz?")
        if not name:
            print("Imię nie może być puste!")
            continue
        elif not name.isalpha():
            print("Liczy i znaki specjalne nie są dozwolone!")
            continue
        else:
            return name


def main():
    print("Witaj w grze Quick Adventure Game!")

    name = ask_name()
    player = Player(name)
    storage = Storage()
    input("Budzisz się w starym magazynie. Pod ścianą widzisz skrzynię. Naciśnij dowolny przycisk, aby do niej podejść"
          "i ją przeszukać.")
    storage.search()

    sewers = Sewers()

# gracz wchodzi do magazynku, zabiera rzeczy, schodzi do kanałów, zabija pająka, leczy się


if __name__ == '__main__':
    main()
