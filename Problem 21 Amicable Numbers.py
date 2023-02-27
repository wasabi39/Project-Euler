#counts the sum of all amicable numbers below 10000
sum_of_amicable_numbers = 0
n = 1
sum_of_divisors = 0
while n < 10000:
    i = 1
    while i <= n / 2:
        if n % i == 0:
            sum_of_divisors += i
        i += 1
    q = 1
    sum_of_amicable_divisors = 0
    while q <= sum_of_divisors / 2 and sum_of_divisors < 10000:
        if sum_of_divisors % q == 0:
            sum_of_amicable_divisors += q
        q += 1
    if n == sum_of_amicable_divisors and n < sum_of_divisors:
        print(n)
        sum_of_amicable_numbers += n + sum_of_divisors
        print(sum_of_divisors)
    n += 1
    sum_of_divisors = 0
print(sum_of_amicable_numbers)