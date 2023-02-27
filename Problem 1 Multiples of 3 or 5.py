print('Enter a number:')
number = int(input())
sum=0
i=1
while i < number:
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
    i += 1
print("The sum of all natural numbers below", number, "that are multiples of 3 or 5 is",sum,'.')