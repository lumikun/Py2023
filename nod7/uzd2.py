# 2. Palindroms
def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    print(s)
    return s == s[::-1]

txt = input("Please input some string: ")
print(is_palindrome(txt))