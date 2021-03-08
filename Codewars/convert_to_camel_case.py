def to_camel_case(text):
    rep = [word.title() for word in text.replace("_", "-").split("-")]
    return "".join(rep) if text[0].isupper() else "".join([rep[0].lower()] + rep[1:])
