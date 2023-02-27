#returns the index of the first Fibonacci number with 1000 digits
f_1 = 1
f_2 = 1
n = 2
fibonacci_found = False
while fibonacci_found == False:
    f_2 += f_1
    f_1 = f_2 - f_1
    n+=1
    if len(str(f_2)) >= 1000:
        fibonacci_found = True
print (n)