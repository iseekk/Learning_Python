def format_words(words):
    if words:
        return ", ".join(word for word in words if word)[::-1].replace(',', 'dna ', 1)[::-1]
    else:
        return ""


if __name__ == '__main__':
    print(format_words(['one', 'two', 'three', 'four']))
    print(format_words(['one']))
    print(format_words(['one', '', 'three']))
    print(format_words(['', '', 'three']))
    print(format_words(['one', 'two', '']))
    print(format_words([]))
    print(format_words(None))
    print(format_words(['']))
