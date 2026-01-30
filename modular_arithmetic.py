# Step 1: Function to perform Modular Addition
def mod_add(a, b, m):
    return (a + b) % m


# Step 2: Function to perform Modular Multiplication
def mod_mul(a, b, m):
    return (a * b) % m


# Step 3: Function to perform Modular Exponentiation
def mod_exp(base, exp, m):
    result = 1
    base = base % m

    while exp > 0:
        if exp & 1:
            result = (result * base) % m
        base = (base * base) % m
        exp >>= 1

    return result


# Step 4: Function to compute Modular Inverse
def mod_inv(a, m):
    t, newt = 0, 1
    r, newr = m, a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr

    if r != 1:
        return None

    return t % m


print("MODULAR ARITHMETIC OPERATIONS\n")

print("1. Modular Addition")
print("2. Modular Multiplication")
print("3. Modular Exponentiation")
print("4. Modular Inverse")

choice = int(input("\nEnter your choice: "))

# Step 5: Perform operation based on user choice
if choice == 1:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    m = int(input("Enter modulus m: "))
    print("Result:", mod_add(a, b, m))

elif choice == 2:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    m = int(input("Enter modulus m: "))
    print("Result:", mod_mul(a, b, m))

elif choice == 3:
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent: "))
    m = int(input("Enter modulus m: "))
    print("Result:", mod_exp(base, exp, m))

elif choice == 4:
    a = int(input("Enter number a: "))
    m = int(input("Enter modulus m: "))
    inv = mod_inv(a, m)

    if inv is None:
        print("Result: Modular inverse does not exist")
    else:
        print("Result:", inv)

else:
    print("Invalid choice")

#OUTPUT:
MODULAR ARITHMETIC OPERATIONS

1. Modular Addition
2. Modular Multiplication
3. Modular Exponentiation
4. Modular Inverse

Enter your choice: 1
Enter a: 4
Enter b: 5
Enter modulus m: 7
Result: 2
