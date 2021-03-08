class Critter(object):

    objects = []

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.__class__.objects.append(self)

    def __str__(self):
        reply = '{n} - hunger: {h}, boredom: {b}'.format(n=self.name, h=self.hunger, b=self.boredom)
        return reply

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print('Nazywam się {name} i jestem {mood}.'.format(name=self.name, mood=self.mood))
        self.__pass_time()

    def eat(self, food=4):
        print('Mniam, mniam. Dziękuję.')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Hura!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit1 = Critter(name='Burek')
    crit2 = Critter(name='Azor', hunger= 5)
    crit3 = Critter(name='Fafik', boredom= 4)
    crit4 = Critter(name='Puszek', hunger= 2, boredom= 7)
    crit5 = Critter(name='Diego', hunger= 6, boredom= 3)

    choice = None
    while choice != "0":
        print("""
     Opiekun zwierzaka
     0 - zakończ
     1 - słuchaj swoich zwierzaków
     2 - nakarm swoje zwierzaki
     3 - pobaw się ze swoimi zwierzakami
     """)
        choice = input("Wybierasz: ")
        print()
        if choice == "0":
            print("Do widzenia.")
        elif choice == "1":
            for obj in Critter.objects:
                obj.talk()
        elif choice == "2":
            while True:
                try:
                    food = int(input('Podaj ilość pożywienia: '))
                except ValueError:
                    print('Wprowadź liczbę!')
                    continue
                else:
                    break
            for obj in Critter.objects:
                obj.eat(food)
        elif choice == "3":
            while True:
                try:
                    fun = int(input('Podaj ilość czasu: '))
                except ValueError:
                    print('Wprowadź liczbę!')
                    continue
                else:
                    break
            for obj in Critter.objects:
                obj.play(fun)
        elif choice == '9':
            for obj in Critter.objects:
                print(obj)
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
