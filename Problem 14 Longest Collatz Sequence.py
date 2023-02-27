i = 2
n = 2
biggest_counter = 0
while n < 1000000:
    i = n
    counter = 0
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            counter += 1
        else:
            i = 3 * i + 1
            counter +=1
    if counter > biggest_counter:
        biggest_counter = counter
        number_with_biggest_counter = n
    n += 1
print(number_with_biggest_counter)