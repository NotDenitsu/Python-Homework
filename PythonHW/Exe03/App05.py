t = []
t.append(str(input()))
t.append(str(input()))
t.append(str(input()))

for x in range (0, len(t)):
    if x != len(t) - 1:
        print(t[x] + ",", end = "")
    else:
        print(t[x])