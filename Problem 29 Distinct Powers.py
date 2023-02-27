a = 2
b = 2
distinct_powers = []
while b <= 100:
    if a**b not in distinct_powers:
        distinct_powers.append(a**b)
    if a == 100:
        b += 1
        a = 2
    else:
        a += 1
print(len(distinct_powers))