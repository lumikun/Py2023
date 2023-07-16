# 3. Vai ir pangramma?


def is_pangram(txt, a='abcdefghijklmnopqrstuwxyz'):
    return not set(a) - set(txt.lower())


print(is_pangram("abc foo"))    # -> False
print(is_pangram("The Quick Borwn Fox jumps over the lazy dog"))    # -> True
print(is_pangram("The five boxing wizards jump quikcly"))   # -> True
