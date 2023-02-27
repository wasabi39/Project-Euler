print('Enter a number:')
number = int(input())
print('The prime factors of',number,'are:')
divisor = 2
while divisor <= number:
    if number % divisor == 0:
        print(divisor)
        largest_divisor = divisor
        number = int(number / divisor)
    divisor += 1  
