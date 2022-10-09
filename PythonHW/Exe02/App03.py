
numbers = input().split(",")
sum = 0

for x in numbers:
    sum += int(x)

avg = sum / len(numbers)
print("%.2f" % float(avg))

