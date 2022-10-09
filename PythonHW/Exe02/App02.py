n = int(input())
myList = []

for x in range(n):
    myList.append(int(input()))
myList.sort()
print(myList)
print(myList[len(myList) - 2])