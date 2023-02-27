T = 40755      #Goal of this script is to find the next number that is triangular, pentagonal and hexagonal, assuming the number 40755 is all 3 things.
P = 40755
H = 40755
T_counter = 285
P_counter = 165
H_counter = 143
triangle_number_found = False
while triangle_number_found == False:
    if T <= P and T <= H:               #we always increase the smallest number of P, T and H.
        T_counter += 1
        T = (T_counter * (T_counter + 1)) / 2
    elif P <= H:
        P_counter +=1
        P = (P_counter * (3 * P_counter - 1)) / 2
    else:
        H_counter += 1
        H = (H_counter * (2 * H_counter - 1))
    if T == P and T == H:
        triangle_number_found = True
print(H)
