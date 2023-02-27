#assumptions:
#a<b<c
#only one solution satisfies a+b+c=1000 and a*a+b*b=c*c
#goal is to find a*b*c
#in this program we check all numbers a, b and c for which a+b+c=1000 and a<b<c until we find a combination that satisfies a*a+b*b=c*c.
a = 1
b = 2
c = 997
triplet_found = False
while triplet_found == False:
    if a*a+b*b==c*c and a+b+c==1000:
        product_of_triplets = a*b*c
        break
    elif b >= c:
        a += 1
        b = a + 1
        c = 1000 - a - b
    else:
        b +=1
        c -=1
print(product_of_triplets)