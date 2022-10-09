t = str(input()).split(" ")
targetWord = str(input())

for x in t:
    if x.casefold() == targetWord.casefold():
        t.remove(x)

t[0] = t[0].capitalize()

for x in t:
    print(x + " ", end ="")