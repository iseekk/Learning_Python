def london_city_hacker(journey):
    bus = False
    cost = 0
    for s in journey:
        if isinstance(s, int) and bus:
            bus = False
        elif isinstance(s, int):
            cost += 1.5
            bus = True
        else:
            cost += 2.4
    return "£{:.2f}".format(cost)


print(london_city_hacker(['Piccidilly', 56, 93, 243]), "£7.80")
