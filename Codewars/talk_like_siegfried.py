def week1(text):
    for i in range(len(text) - 1):
        if text[i].lower() == "c" and (text[i+1].lower() == "i" or text[i+1].lower() == "e"):
            if text[i] == "c":
                text[i] = "s"
            else:
                text[i] = "S"
        elif text[i].lower() == "c" and text[i+1].lower() != "h":
            if text[i] == "c":
                text[i] = "k"
            else:
                text[i] = "K"
    return text


def week2(text):
    indices = []

    for i in range(len(text) - 1):
        if text[i].lower() == "p" and text[i + 1].lower() == "h":
            indices.append(i + 1)
            if text[i] == "p":
                text[i] = "f"
            else:
                text[i] = "F"

    for count, index in enumerate(indices):
        del text[index - count]
    return text


def week3(text):
    indices = []

    for i in range(len(text) - 1):
        if text[i].lower() == "e" and text[i - 2].isalpha() and text[i - 3].isalpha() and not text[i + 1].isalpha():
            indices.append(i)
        if text[i].isalpha() and text[i].lower() == text[i + 1].lower():
            indices.append(i + 1)

    for count, index in enumerate(indices):
        del text[index - count]
    return text


def week4(text):
    indices = []

    for i in range(len(text) - 1):
        if text[i].lower() == "t" and text[i + 1].lower() == "h":
            if text[i] == "t":
                text[i] = "z"
                indices.append(i+1)
            else:
                text[i] = "Z"
                indices.append(i+1)
        elif text[i].lower() == "w" and text[i + 1].lower() == "r":
            indices.append(i)
            if text[i] == "W":
                text[i + 1] = "R"
        elif text[i].lower() == "w":
            if text[i + 1].lower() == "h":
                indices.append(i + 1)
            if text[i] == "W":
                text[i] = "V"
            else:
                text[i] = "v"

    for count, index in enumerate(indices):
        del text[index - count]
    return text


def week5(text):
    indices = []

    for i in range(len(text) - 1):
        if text[i].lower() == "o" and text[i + 1].lower() == "u":
            indices.append(i)
            if text[i] == "o":
                text[i] = "u"
            else:
                text[i] = "U"
        elif text[i].lower() == "a" and text[i+1].lower() == "n":
            if text[i] == "a":
                text[i] = "u"
            else:
                text[i] = "U"
        elif text[i].lower() == "i" and text[i + 1].lower() == "n" and text[i + 2].lower() == "g" \
                                    and (i + 3 == len(text) or not text[i + 3].isalpha()):
            text[i + 2] = "k"
        elif text[i].lower() == "s" and text[i + 1].lower() == "m" and (i + 1 >= 0 or not text[i - 1].isalpha()):
            if text[i] == "s":
                text[i] = "sch"
            else:
                text[i] = "Sch"

    for count, index in enumerate(indices):
        del text[index - count]
    return text


def siegfried(week, txt):
    txt_list = [_ for _ in txt] + [" "]
    weeks = [week1, week2, week3, week4, week5]

    for i in range(week):
        txt_list = weeks[i](txt_list)

    return "".join(i for i in txt_list).rstrip()




import re

def dif_siegfried(week, txt):
    weeks = [
        [['ci','si'],['ce','se'],['c(?!h)','k']],
        [['ph','f']],
        [['e(?<=\w{4})(?!\w)', ''], ['([A-Za-z])(\\1)', '\1']],
        [['th', 'z'], ['wr', 'r'], ['wh?', 'v']],
        [['ou', 'u'], ['an', 'un'], ['ing(?!\w)', 'ink'], ['(?<!\w)sm', 'schm']]
    ]
    def replacementText(x):
        if replace == '\1': return x.group(0)[0]
        if x.group(0)[0].isupper(): return replace.capitalize()
        else: return replace
    for i in range(week):
        for [orig, replace] in weeks[i]:
            txt = re.compile(orig, re.I).sub(replacementText, txt);
    return txt;


english = ''.join("""
This is KAOS!! We don't play with Code-Wars here!!
 So there will be trouble for you this time Mr Maxwell Smart!
 We have received all the photographic evidence we need so choose carefully what you say next!
 I hope you will co-operate with KAOS and do exactly what we want Mr Smart otherwise I won't be happy with you!
 In fact, if you misbehave that would make me very unhappy indeed...
 And you certainly would not want to make me unnecesarily cross would you Mr Maxwell Smart?
""".split('\n'))

afterWeek1 = ''.join("""
This is KAOS!! We don't play with Kode-Wars here!!
 So there will be trouble for you this time Mr Maxwell Smart!
 We have reseived all the photographik evidense we need so choose karefully what you say next!
 I hope you will ko-operate with KAOS and do exaktly what we want Mr Smart otherwise I won't be happy with you!
 In fakt, if you misbehave that would make me very unhappy indeed...
 And you sertainly would not want to make me unnesesarily kross would you Mr Maxwell Smart?
""".split('\n'))

afterWeek2 = ''.join("""
This is KAOS!! We don't play with Kode-Wars here!!
 So there will be trouble for you this time Mr Maxwell Smart!
 We have reseived all the fotografik evidense we need so choose karefully what you say next!
 I hope you will ko-operate with KAOS and do exaktly what we want Mr Smart otherwise I won't be happy with you!
 In fakt, if you misbehave that would make me very unhappy indeed...
 And you sertainly would not want to make me unnesesarily kross would you Mr Maxwell Smart?
""".split('\n'))

afterWeek3 = ''.join("""
This is KAOS!! We don't play with Kod-Wars her!!
 So ther wil be troubl for you this tim Mr Maxwel Smart!
 We hav reseived al the fotografik evidens we ned so chos karefuly what you say next!
 I hop you wil ko-operat with KAOS and do exaktly what we want Mr Smart otherwis I won't be hapy with you!
 In fakt, if you misbehav that would mak me very unhapy inded...
 And you sertainly would not want to mak me unesesarily kros would you Mr Maxwel Smart?
""".split('\n'))

afterWeek4 = ''.join("""
Zis is KAOS!! Ve don't play viz Kod-Vars her!!
 So zer vil be troubl for you zis tim Mr Maxvel Smart!
 Ve hav reseived al ze fotografik evidens ve ned so chos karefuly vat you say next!
 I hop you vil ko-operat viz KAOS and do exaktly vat ve vant Mr Smart ozervis I von't be hapy viz you!
 In fakt, if you misbehav zat vould mak me very unhapy inded...
 And you sertainly vould not vant to mak me unesesarily kros vould you Mr Maxvel Smart?
""".split('\n'))

afterWeek5 = ''.join("""
Zis is KAOS!! Ve don't play viz Kod-Vars her!!
 So zer vil be trubl for yu zis tim Mr Maxvel Schmart!
 Ve hav reseived al ze fotografik evidens ve ned so chos karefuly vat yu say next!
 I hop yu vil ko-operat viz KAOS und do exaktly vat ve vunt Mr Schmart ozervis I von't be hapy viz yu!
 In fakt, if yu misbehav zat vuld mak me very unhapy inded...
 Und yu sertainly vuld not vunt to mak me unesesarily kros vuld yu Mr Maxvel Schmart?
""".split('\n'))

print(siegfried(5, english))
# print(siegfried(2, english), "\n", afterWeek2, "\n")
# print(siegfried(3, english), "\n", afterWeek3, "\n")
# print(siegfried(4, english), "\n", afterWeek4, "\n")
# print(siegfried(5, english), "\n", afterWeek5, "\n")



