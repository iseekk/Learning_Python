def max_ball(v0):
    rep = []
    t = 0.1
    while True:
        h = v0 * 0.277778 * t - 0.5 * 9.81 * t * t
        if len(rep) and h < rep[-1]:
            break
        rep.append(h)
        t += 0.1
    return len(rep)
