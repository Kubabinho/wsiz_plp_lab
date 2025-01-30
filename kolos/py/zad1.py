import re

def most_char(s):
    maxL = 0
    currL = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            currL += 1
        else:
            maxL = max(maxL, currL)
            currL = 1

    maxL = max(maxL, currL)

    return maxL

while True:
    toCheck = input("podaj cos do psrawdzenia")
    if re.fullmatch("[a-z]+", toCheck):
        print(most_char(toCheck))
        break
    else:
        print("daj same litery")
