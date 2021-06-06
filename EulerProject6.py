total1 = 0
total2 = 0

for i in range(101):
    total1 += i * i
    total2 += i

total2 *= total2
print(total2 - total1)