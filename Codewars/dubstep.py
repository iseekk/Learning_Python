def dubstep(string):
    return " ".join(string.replace("WUB", " ").split())


if __name__ == '__main__':
    print(dubstep("WUBAWUBBWUBCWUB"))
    print(dubstep("WUBWUBAWUBWUBBWUBWUBCWUBWUB"))
    print(dubstep("AWUBBWUBC"))
