#finds the smallest pair of pentagonal numbers p1 and p2, for which p1 + p2 is a pentagonal number and p1 - p2 is a pentagonal number.
pentagonal_numbers = []
for n in range(1,3000):
    pentagonal_numbers.append(int(n * (3*n-1) / 2))
for n in range(1,3000):
    for q in range (1,n):
        if int((n * (3*n-1) / 2) + (q * (3*q-1) / 2)) in pentagonal_numbers:
            if int((n * (3*n-1) / 2) - (q * (3*q-1) / 2)) in pentagonal_numbers:
                print(n, q,int((n * (3*n-1) / 2) - (q * (3*q-1) / 2)))
            else:
                continue
        else:
            continue