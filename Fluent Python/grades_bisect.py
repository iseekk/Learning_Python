import bisect


def grade(score, breakpoints=(30, 60, 75, 90, 100), grades="123456"):
    return grades[bisect.bisect(breakpoints, score)]


if __name__ == "__main__":
    print("\n".join(f"{s} pkt: {grade(s)}" for s in [33, 99, 77, 70, 89, 90, 100]))
