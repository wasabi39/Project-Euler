print('Enter a number:')
number = int(input())
i=1
j=2
sum = 0
while j <= number:
    print(j)
    if j % 2 == 0:
        sum += j
        
    j = i+j
    i = j-i
print(sum)