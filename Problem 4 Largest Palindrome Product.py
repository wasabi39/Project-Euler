factor_1 = 999
factor_2 = 999
palindrome_found = False
largest_palindrome = 100001
while factor_2 > 800:
    product = factor_1 * factor_2
    product_as_string = str(product)
    if product_as_string[0] ==  product_as_string[5] and product_as_string[1] ==  product_as_string[4] and product_as_string[2] ==  product_as_string[3] and product > largest_palindrome:
        largest_palindrome = product
        palindrome_found = True
    if factor_1 * factor_2 < largest_palindrome or factor_1 < 200:
        factor_2 -= 1
        factor_1 = 999
    else:
        factor_1 -= 1
print(largest_palindrome)