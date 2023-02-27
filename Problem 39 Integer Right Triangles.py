# we seek to find the perimeter p between 1 and 1000 with the highest number of solutions to a*a+b*b=c*c
# assumptions:
#a<b<c
#p=a+b+c where p is the perimeter
#c > 1/3p and c < 1/2p
a = 1
b = 2
c = 3
sum_of_solutions = 0
p = 6
optimal_solution = 0
max_number_of_solutions = 0

while p <= 1000:
    if p % 3 == 0:
        c = int(p / 3)
        a = 1
        b = p - a - c
    elif p % 3 == 1:
        c = int(p / 3 - 1)
        a = 1
        b = p - a - c
    else:
        c = int(p / 3 - 2)
        a = 1
        b = p - a - c
    while c <= p / 2:
        if a*a+b*b==c*c and a+b+c==p:
            sum_of_solutions += 1
            if sum_of_solutions > max_number_of_solutions:
                max_number_of_solutions = sum_of_solutions
                optimal_solution = p
        if a < b - 2:
            a += 1
            b -= 1
        else:
            c += 1
            a = 1
            b = p - c - a
    p += 1
    sum_of_solutions = 0
print(optimal_solution)
print(max_number_of_solutions)