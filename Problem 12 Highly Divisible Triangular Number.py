import math #this program finds the smallest triangular number with over 500 divisors

sum_of_divisors = 0
n = 500
solution_found = False
list_of_triangular_numbers = []
for n in range(10,20000):
    triangular_number = int(n * (n + 1) / 2)        #this generates the first 20,000 triangular numbers and adds them to a list
    list_of_triangular_numbers.append(triangular_number)
    for i in range(1,int(math.sqrt(triangular_number))): #this checks the number of divisors with a sieve
        if triangular_number % i == 0:
            if triangular_number / i == i:
                sum_of_divisors += 1
            else:
                sum_of_divisors += 2
    if sum_of_divisors > 500:
        break
    else:
        sum_of_divisors = 0             
print(triangular_number)