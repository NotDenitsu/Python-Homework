n = int(input())
evenSum = 0
oddSum = 0

for x in range(n):
    currentNumber = int(input())
    if currentNumber % 2 == 0:
        evenSum += currentNumber
    else:
        oddSum += currentNumber

print("Сума четни: " + str(evenSum))
print("Сума нечетни: " + str(oddSum))