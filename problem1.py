a = 3
sum = 0
for a in range(999):
    a += 1
    if a % 3 == 0 or a % 5 == 0 :
        sum += a

print(sum)