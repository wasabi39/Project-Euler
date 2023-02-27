print('Enter a number:')
max_number = int(input())
i = 1
j = 1
sum_of_squares = 0
square_of_sum = 0
while i <= max_number:
    sum_of_squares += i*i
    i+=1
while j <= max_number:
    square_of_sum += j
    j+= 1
square_of_sum = square_of_sum * square_of_sum
difference = square_of_sum - sum_of_squares
print(difference)
print(sum_of_squares)
print(square_of_sum)