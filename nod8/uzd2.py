#!/usr/bin/env python3
# 2. Vārdnīcu labotājs

def replace_dict_value(d, bad_val, good_val):
    for k, v in d.items():
        if (v == bad_val):
            d[k] = good_val

test_dict = { 'a': 5, 'b': 6, 'c': 5 , 'g': 9, 'f': 10, 'e': 5}
print(f"The Dictionary: {test_dict}!")
replace_dict_value(test_dict, 5, 10)
print(f"The Dictionary after replacing by value: {test_dict}")
