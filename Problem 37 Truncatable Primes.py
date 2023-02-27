#identifies primes that are truncatable both from the left and from the right.
prime_list = []
potential_truncatable = []
max_prime = 1000000
not_prime = set()
for n in range(2,max_prime):
    if n in not_prime:
        continue
    for q in range(2*n,max_prime,n):
        not_prime.add(q)
    prime_list.append(n)
    if "4" in str(n):
        continue
    elif "6" in str(n):
        continue
    elif "8" in str(n):
        continue
    elif "0" in str(n):
        continue
    else:
        potential_truncatable.append(n) #all primes including a 4, 6, 8 or 0 is immediately discarded, as they cannot be truncatable and this saves processing time drastically.
sum = 0
solutions_found = 0
potential_truncatable = potential_truncatable[4:]
print(len(potential_truncatable))
for n in potential_truncatable:
    n_as_string_1 = str(n)
    n_as_string_2 = str(n)
    truncatable = True
    while len(n_as_string_1) > 1:
        n_as_string_1 = n_as_string_1[1:]
        if int(n_as_string_1) not in prime_list:
            truncatable = False
            break
    while len(n_as_string_2) > 1:
        n_as_string_2 = n_as_string_2[0:len(n_as_string_2)-1]
        if int(n_as_string_2) not in prime_list:
            truncatable = False
            break
    if truncatable == True:
        sum += n
        solutions_found += 1
        print(n)
print(sum)
print(solutions_found)