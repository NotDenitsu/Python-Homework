t = str(input())
tReversed = ""
tReversed = reverse(t)

#for x in range(len(t) - 1, -1, -1):
    #tReversed += t[x]

if t == tReversed:
    print("Да")
else:
    print("Не")