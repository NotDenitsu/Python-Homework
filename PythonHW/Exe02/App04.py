numbers = input().split(",")
diff = []
sum = 0

for x in numbers:
    sum += int(x)

avg = sum / len(numbers)

for x in numbers:
    diff.append(int(x) - avg)

for x in range(len(diff) - 1):
    diff[x] = abs(diff[x])

print("Средна стойност: " + "%.5f" % avg)
print("Число: " + str(numbers[diff.index(max(diff))]))