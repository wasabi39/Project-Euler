#solution to https://projecteuler.net/problem=64
import math
n = 1
sum_of_uneven_periods = 0
while n <= 10000:
    if int(math.sqrt(n))**2 == n:
        n += 1
        continue
    m = 0
    d = 1
    a = int(math.sqrt(n))
    q = 0
    m1 = int(d*a-m)
    d1 = int((n - m1**2) / d)
    a1 = int((math.sqrt(n)+m1)/d1)
    a_list = []
    while q < 2:
        m=int(d*a-m)
        d=int((n - m**2) / d)
        a = int((math.sqrt(n)+m)/d)
        a_list.append(a)
        if m1 == m and d1 == d and a1 == a:
            q += 1
    if(len(a_list) - 1) % 2 == 1:
        sum_of_uneven_periods += 1
    n += 1
print(sum_of_uneven_periods)
