# 1. Simbolu biežums
# a un b versija

def get_char_count(s):
    d = {}
    txt = str(s)
    for c in txt:
        d[c] = d.get(c, 0)+1
    return d


print(get_char_count("hubba bubba"))
print(get_char_count(1234444567891099))
