# negative quadratics
import re
import math

def factorize_quadratic(a,b,c):
    b2 = b**2
    fourac = 4*a*c
    discriminant = math.sqrt(b2-fourac)
    root1 = int((-b + discriminant) / (2*a))
    root2 = int((-b - discriminant) / (2*a))

    print(f"Roots: {root1}, {root2}")

quad = input('Enter the Quadratic: ')

abc_match = re.search(r"([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d*)", quad)

ac_match = re.search(r"([+-]?\d*)x\^2([+-]?\d*)", quad)

ab_match = re.search(r"([+-]?\d*)x\^2([+-]?\d*)x", quad)


if abc_match:
    a, b, c = abc_match.groups()

    a = int(a) if a and a != '-' else -1 if a == '-' else 1
    b = int(b) if b else 0
    c = int(c) if c else 0
    
    print(a,b,c)
    factorize_quadratic(a,b,c)

elif ab_match:
    a, b = ab_match.groups()
    a = int(a) if a and a != '-' else -1 if a == '-' else 1
    b = int(c) if b else 0

    print(a, b, 0)
    factorize_quadratic(a, b, 0)

elif ac_match:
    a, c = ac_match.groups()

    a = int(a) if a and a != '-' else -1 if a == '-' else 1
    c = int(c)

    print (a, 0, c)
    factorize_quadratic(a, 0, c)

else:
    print("Invalid input")

# reg ex cares about case 
# can i get all the reg ex into one 