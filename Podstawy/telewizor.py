import sys


class Television(object):
    def __init__(self, volume=0, channel=1):
        self.volume = volume
        self.channel = channel

    @staticmethod
    def off():
        print('\n\nWyłączono telewizor!\n\n')
        sys.exit()

    def display(self):
        print('''         ___________________
        |                 {c} |
        |                   |
        |      vol: {v}       |
        |___________________|
               ___|___
        
        1: Zmiana głośności (+/-)
        2: Zmiana kanału (1-9)
        
        0: Wyłącz telewizor'''.format(c=self.channel, v=self.volume))

    def change_vol(self):
        while True:
            choice = input("Wprowadź '+' lub '-'. Aby powrócić do menu wprowadź '0'.")
            if choice == '+':
                if self.volume > 8:
                    print('Max volume!')
                else:
                    self.volume += 1
                    print('vol: {v}'.format(v=self.volume))
                continue
            elif choice == '-':
                if self.volume < 1:
                    print('Mute')
                else:
                    self.volume -= 1
                print('vol: {v}'.format(v=self.volume))
                continue
            elif choice == '0':
                break
            else:
                continue

    def change_channel(self):
        while True:
            try:
                choice = int(input("Wprowadź numer kanału (1-9). Aby powrócić do menu, wprowadź '0'."))
            except ValueError:
                print('Wprowadź cyfrę z zakresu 1-9!')
            if choice == self.channel:
                print('Obecnie oglądasz ten kanał!')
                break
            elif choice == 0:
                break
            elif choice not in range(1, 10) and choice != 0:
                print('Wprowadź cyfrę z zakresu 1-9!')
                continue
            else:
                self.channel = choice
                break

    def menu(self):
        SWITCH = {1: self.change_vol,
                  2: self.change_channel,
                  0: self.off}
        while True:
            self.display()
            try:
                key = int(input())
            except ValueError:
                print('Opcje w menu wybierz za pomocą liczb')
            else:
                SWITCH.get(key, self.display)()
            finally:
                input('Aby zakończyć program naciśnij ENTER.')


def main():
    tv = Television()
    tv.menu()


main()
