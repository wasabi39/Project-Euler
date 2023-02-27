start = 1
spiral_number = 2
sum = 1
step_increase_in_value = 8 * spiral_number - 3
value_at_step = 6

while spiral_number <=  501:
    print(value_at_step)
    sum += value_at_step * 4
    step_increase_in_value = 8 * spiral_number - 3
    value_at_step = value_at_step + step_increase_in_value
    spiral_number += 1
print(sum)