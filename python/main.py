print("This is balanced")


# fanvue
# wavespeed ai seedream
# videa kling AI

def space_jam(text):
    text = text.replace(" ", "").upper()
    result = ""
    for i in range(len(text)):
        if i != 0 and i < len(text):
            result += (f" {text[i]} ")
        elif i == 0:
            result += (f"{text[i]} ")
        else:
            result += (f" {text[i]}")
    return result

a = space_jam("freeCodeCamp")
b = space_jam("   free   Code   Camp   ")
print(a)
print(b)