n = 1
champernowne = ""
while len(champernowne) <= 1000000:
    champernowne += str(n)
    n += 1
print(int(champernowne[0])*int(champernowne[9])*int(champernowne[99])*int(champernowne[999])*int(champernowne[9999])*int(champernowne[99999])*int(champernowne[999999]))