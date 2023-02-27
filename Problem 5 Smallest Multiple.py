print('Enter a number:')        #This program finds the smallest denominator that can be divided by each number from 1 up to the number inputted by the user with a remainder.
largest_factor = int(input())
number = 1                      #"number" is the smallest number that can be divided by all integers from 1 to i.
i = 1                          
j= 1
while i < largest_factor:       #We let the script run until i is equal to number the user entered.
    if number % i != 0:         #If "number" can be divided by i with no remainder, no issue. If not, we multiply "number" by the smallest possible integer that makes "number" divisble by i.
        while j <= i:
            if (number * j) % i == 0:
                number = number * j
                j = i+1
            else:
                j += 1
    i += 1
    j=1    
print(number)