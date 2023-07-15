# 1. Simbolu biežums

def get_char_count(txt: str):
    d = {}
    for c in txt:
        d[c] = d.get(c, 0)+1
    return d

print(get_char_count("hubba bubba"))
