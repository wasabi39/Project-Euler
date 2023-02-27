import math
print('Enter a number:')
number_entered = int(input())
list_of_primes = [2]
sum_of_primes = 2
current_number = 3
is_prime = True
while current_number < number_entered:
    for prime in list_of_primes:
        if current_number % prime == 0:             #if our current number can be divided by a prime, it isn't a prime and the loop ends
            is_prime = False
            break
        elif math.sqrt(current_number) < prime:
            is_prime = True
            break
    if is_prime == True:                            #if the current number couldn't be divided by any prime, it is added to the list of primes
        list_of_primes.append(current_number)
        sum_of_primes += current_number
    current_number += 2
print(sum_of_primes)
