abundant_numbers = []
for n in range(12,20162):
    if n not in abundant_numbers:
        divisor_sum = 0
        for q in range(1,int((n+3)/2)):
            if n % q == 0:
                divisor_sum += q
        if divisor_sum > n:
            abundant_numbers.append(n)
abundant_sums = []
sum_of_abundant_sums = 0
print("hi")
for b in range(1,20162):
    for p in abundant_numbers:
        if p > b:
            break
        elif b - p in abundant_numbers:
            sum_of_abundant_sums += b
            break
sum_of_not_abundant = 20161 * 20162 / 2 - sum_of_abundant_sums
print(sum_of_not_abundant)
            