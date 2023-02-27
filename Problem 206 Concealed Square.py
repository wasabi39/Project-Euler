import math

print(math.sqrt(1020304050607080900))
print(math.sqrt(1929394959697989990))

number = 1010101010
found = False
while found == False:
    square = number ** 2
    string = str(square)
    if string[0] == "1":
        if string[2] == "2":
            if string[4] == "3":
                if string[6] == "4":
                    if string[8] == "5":
                        if string[10] == "6":
                            if string[12] == "7":
                                if string[14] == "8":
                                    if string[16] == "9":
                                        if string[18] == "0":
                                            found = True
                                            print(number)
                                            break
        
    number += 10
print(square)