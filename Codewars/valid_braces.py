def valid_braces(string):
    braces = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for brace in string:
        if brace in braces.keys():
            stack.append(brace)
        elif len(stack) == 0 or braces[stack.pop()] != brace:
            return False
    return not stack


if __name__ == '__main__':
    print(valid_braces("{([])}"))
    print(valid_braces("{()[])}"))
