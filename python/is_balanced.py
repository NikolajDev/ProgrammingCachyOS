def check_vowels(left_text, right_text):
    left = 0
    right = 0
    vowels = "aeiou"
    for char in left_text:
        if char in vowels:
            left += 1
    for char in right_text:
        if char in vowels:
            right += 1
    return left == right


def is_balanced(s: str):
    s = s.lower()
    mid = len(s) // 2
    length = len(s)
    if length % 2 == 0:
        return check_vowels(s[:mid], s[mid:])
    else:
        return check_vowels(s[:mid], s[mid + 1 :])


print(is_balanced("racecar"))
