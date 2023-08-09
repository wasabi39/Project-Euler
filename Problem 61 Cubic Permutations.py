cubic_map = {}
i = 1
solution_found = False

while solution_found == False:
    i_cubed = i ** 3
    
    key = ''.join(sorted(str(i_cubed)))

    if key in cubic_map.keys():
        cubic_map[key][1] += 1
        if cubic_map[key][1] == 5:
            print(cubic_map[key][0] ** 3)
            solution_found = True
    else:
        cubic_map[key] = [i, 1]
    i += 1
    
