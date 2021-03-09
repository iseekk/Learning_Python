from enum import Enum


class Numbers(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    thirty = 30
    forty = 40
    fifty = 50
    sixty = 60
    seventy = 70
    eighty = 80
    ninety = 90


def number_to_name(number):
    if number < 20:
        return Numbers(number).name
    elif number < 100 and not number % 10:
        return Numbers(number).name
    elif number < 100:
        return f"{Numbers(number // 10 * 10).name}-{Numbers(number % 10).name}"
    elif not number % 100:
        return f"{Numbers(number // 100).name} hundred"
    else:
        return f"{Numbers(number // 100).name} hundred {number_to_name(number % 100)}"


def sort_by_name(arr):
    return sorted(arr, key=number_to_name)


print(sort_by_name([1, 2, 3, 4, 5]))
