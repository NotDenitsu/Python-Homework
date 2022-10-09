numbers = input().split(",")
sum = 0

for x in numbers:
    sum += abs(float(x))

print(int(sum))
