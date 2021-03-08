from time import time, strftime, localtime
from sys import exit
from datetime import timedelta

RUNNING = False
LAP = 0
START_TIME = ""
NEW_LAP = ""


def start_time(t):
    global RUNNING, START_TIME, NEW_LAP
    if not RUNNING:
        START_TIME = t
        NEW_LAP = START_TIME
        time_to_write = strftime("%H:%M:%S", localtime(START_TIME))
        with open("time.txt", "a") as f:
            f.write(f'Start:\t{time_to_write}\n'
                    f'-------------------\n'
                    f'LAP\t\t\tTIME\n'
                    f'-------------------\n')
        print("Stopwatch is running.")
        RUNNING = True
    else:
        print("Stopwatch is already running.")


def lap_time(t):
    global RUNNING, NEW_LAP, LAP
    if RUNNING:
        time_to_write = str(timedelta(seconds=t - NEW_LAP))[:-3]
        LAP += 1
        with open("time.txt", "a") as f:
            f.write(f'{LAP}\t\t{time_to_write}\n')
        print(f'Lap {LAP} time: {time_to_write}')
        NEW_LAP = t
    else:
        print("Start stopwatch firstly.")


def stop_time(t):
    global RUNNING, START_TIME
    if RUNNING:
        total = str(timedelta(seconds=t-START_TIME))[:-3]
        with open("time.txt", "a") as f:
            f.write(f'TOTAL:\t{total}\n\n')
        print("Stopwatch stopped.")
        RUNNING = False
    else:
        print("Stopwatch is not running.")


def program_exit(t):
    exit()


def print_menu():
    print("\nMENU\n"
          "1. Start\n"
          "2. Lap\n"
          "3. Stop\n"
          "--------\n"
          "5. Quit\n")


SWITCH = {1: start_time,
          2: lap_time,
          3: stop_time,
          5: program_exit,
          }


if __name__ == '__main__':

    while True:
        print_menu()
        try:
            key = int(input())
        except ValueError:
            continue
        else:
            SWITCH.get(key)(time())