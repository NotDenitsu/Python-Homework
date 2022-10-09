numbers = input().split(",")

sum = 0

for x in numbers:
    if int(x) > 15 and int(x) % 3 == 0:
        sum += int(x)

print(sum)