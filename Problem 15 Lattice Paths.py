import math
print('Enter a number:')
dimensions = int(input())  #dimensions = r
moves = dimensions * 2 #moves = n
binomial_coefficient = (math.factorial(moves) / (math.factorial(dimensions)*math.factorial(moves - dimensions)))
print(int(binomial_coefficient))