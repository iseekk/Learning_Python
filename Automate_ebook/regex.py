import re


def match_num_with_commas(string):
    return re.compile(r'^\d{1,3}(,\d{3})*$').search(string).group()


def match_full_name(string):
    return re.compile(r'^[A-Z]\w+\sNakamoto$').search(string).group()


def match_sentence(string):
    return re.compile(
        r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.IGNORECASE).search(string).group()


def pw_is_strong(string):
    contains_lower = re.compile(r'[a-z]').search(string)
    contains_upper = re.compile(r'[A-Z]').search(string)
    contains_digit = re.compile(r'\d').search(string)
    return True if contains_digit and contains_lower and contains_upper and len(string) >= 8 else False


def my_strip(string, chars=" "):
    new_string = re.compile(r'^[' + re.escape(chars) + r']+').sub("", string)
    return re.compile(r'[' + re.escape(chars) + r']+$').sub("", new_string)


s = ""
print(s.strip(' xoxoe'))
print(my_strip(s, ' xoxoe'))
