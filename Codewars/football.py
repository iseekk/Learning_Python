def men_still_standing(cards):
    red = []
    yellow = []
    still_playing = {"A": 11, "B": 11}

    for card in cards:
        if still_playing["A"] < 7 or still_playing["B"] < 7:
            break

        if card[-1::] == "Y" and card[:-1:] not in red:
            if card[:-1:] not in yellow:
                yellow.append(card[:-1:])
            elif card[:-1:] in yellow:
                red.append(card[:-1:])
                still_playing[card[:1:]] -= 1
        elif card[-1::] == "R" and card[:-1:] not in red:
            red.append(card[:-1:])
            still_playing[card[:1:]] -= 1

    return still_playing["A"], still_playing["B"]


if __name__ == '__main__':
    print(men_still_standing([]))
    # (11,11)
    print(men_still_standing(["A4Y", "A4Y"]))
    # (10,11)
    print(men_still_standing(["A4Y", "A4R"]))
    # (10,11)
    print(men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"]))
    # (9,10)
    print(men_still_standing(["A4R", "A4R", "A4R"]))
    # (10,11)
    print(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"]))
    # (6,11)
