print('Enter a number:') #input the nth prime number you want to find 
prime_sought = int(input())
list_of_primes = [2]
current_number = 2
while len(list_of_primes) < prime_sought:
    for prime in list_of_primes:
        if current_number % prime == 0:             #if our current number can be divided by a prime, it isn't a prime and the loop ends
            is_prime = False
            break
    if is_prime == True:                            #if the current number couldn't be divided by any prime, it is added to the list of primes
        list_of_primes.append(current_number)
    is_prime = True
    current_number += 1
print(list_of_primes[-1])
