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

    root1 = f"+{str(root1)[1:]}" if root1 <= 0 else f"-{str(root1)}" 
    root2 = f"+{str(root2)[1:]}" if root2 <= 0 else f"-{str(root2)}"

    print(f"Factorised: (x{(root1)})(x{root2})")

quad = input('Enter the Quadratic: ')

# reg ex to match quadratic
match = re.search(r"([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d*)", quad)

# extracting a b and c values
if match:
    a, b, c = match.groups()
    # a needs to check for -x aswell
    a = int(a) if a else 1
    #check if b is just x then 1 or if no b then 0
    b = int(b) if b else 0
    c = int(c) if c else 0
    print(a,b,c)
    factorize_quadratic(a,b,c)
else:
    print("Invalid input")



# need to make sure it works for - coefficent of x^2
# need to make sure it works for difference of two squares x^2-16



def factors(x):
    factor_list = []

    for y in range(1,x +1):
        if x % y == 0:
            factor_list.append(y)

    return factor_list
