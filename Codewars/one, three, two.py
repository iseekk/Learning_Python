def sort_by_name(arr):
    number_words = []
    dic = {}
    a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    b = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    for num in arr:
        if not num:
            number_words.append("zero")
            continue

        w = []
        if num // 100 > 0:
            w.append("{} hundred".format(a[int(str(num)[:1])]))

        if 100 > int(str(num)[-2:]) >= 20:
            w.append(b[int(str(num)[-2:-1])])
            if int(str(num)[-1:]) > 0:
                w[-1] += "-"
                w.append(a[int(str(num)[-1:])])
        elif 20 > int(str(num)[-2:]) > 0:
            w.append(a[int(str(num)[-2:])])

        number_words.append(" ".join(n for n in w if n).replace("- ", "-"))

    for n in range(len(arr)):
        dic[number_words[n]] = arr[n]

    return [dic[word] for word in sorted(number_words)]


print(sort_by_name([8, 8, 9, 9, 10, 10]), [8, 8, 9, 9, 10, 10])
print(sort_by_name([1, 2, 3, 4]), [4, 1, 3, 2])
print(sort_by_name([9, 99, 999]), [9, 999, 99])
print(sort_by_name([954, 993, 963, 962, 926, 900]), [900, 954, 993, 963, 962, 926])
