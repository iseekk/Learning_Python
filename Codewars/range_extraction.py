def solution(args):
    rep = []
    ign = 0

    if not args:
        return rep
    else:
        sorted(args)
        rep.append(args[0])
        for n in args[1:-1]:
            if n - 1 == rep[-1]:
                ign = n
                rep.append("-")

            elif rep[-1] == "-" and n - 1 == ign:
                ign = n

            elif rep[-1] == "-" and n - 1 != ign:
                if ign - 1 == rep[-2]:
                    rep.pop()
                    rep.append(ign)
                    rep.append(n)
                else:
                    rep.append(ign)
                    rep.append(n)

            else:
                rep.append(n)

        rep.append(args[-1])

    return ",".join(str(i) for i in rep).replace(",-,", "-")


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '\n-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '\n-3--1,2,10,15,16,18-20')