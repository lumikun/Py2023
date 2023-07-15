#!/usr/bin/env python3
# 3. Vārdnīcu tīrītājs

def clean_dict_value(d, bad_val):
    lst = []
    for k, v in d.items():
        if (v == bad_val):
            lst.append(k)
    for i in lst:
        d.pop(i)


test_dict = { 'a': 5, 'b': 6, 'c': 5, 'e': 4}
print(f"This is the test dict: {test_dict}")
clean_dict_value(test_dict, 5)
print(f"This is the test dict after removing 5: {test_dict}")
