import random
import requests
import time

url = "https://www.olx.pl/d/oferta/nokia-e51-oraz-nokia-7230-CID99-IDINaFh.html#4d8fa82544"


if __name__ == '__main__':
    for i in range(0, 250):
        r = requests.get(url)
        print(i)
        time.sleep(random.randint(1, 3))
