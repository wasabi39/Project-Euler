import math
r = 1
n = 1
sum = 0
while n <= 100:
    if math.factorial(n) / (math.factorial(r)*math.factorial(n-r)) > 1000000:
        sum += 1
    if r == n:
        n += 1
        r = 1
    else:
        r += 1
print(sum)