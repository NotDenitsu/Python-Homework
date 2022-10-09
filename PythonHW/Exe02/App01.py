n = int(input("Брой числа в масива: "))
myList = []

for x in range(n):
    myList.append(int(input()))

print(max(myList))