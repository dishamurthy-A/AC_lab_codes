# =====================================================
# ALGEBRAIC STRUCTURE CHECKS
# GROUP, RING, FIELD (Modulo m)
# Modular Division included as part of FIELD
# =====================================================


# Step 1: Check closure under addition modulo m
def check_closure_add(elements, m):
    for a in elements:
        for b in elements:
            if (a + b) % m not in elements:
                return False
    return True


# Step 2: Check closure under multiplication modulo m
def check_closure_mul(elements, m):
    for a in elements:
        for b in elements:
            if (a * b) % m not in elements:
                return False
    return True


# Step 3: Check associativity of addition modulo m
def check_associativity_add(elements, m):
    for a in elements:
        for b in elements:
            for c in elements:
                if ((a + b) + c) % m != (a + (b + c)) % m:
                    return False
    return True


# Step 4: Check existence of additive identity (0)
def check_identity_add(elements, m):
    if 0 not in elements:
        return False
    for a in elements:
        if (a + 0) % m != a:
            return False
    return True


# Step 5: Check existence of additive inverse for every element
def check_inverse_add(elements, m):
    for a in elements:
        found = False
        for b in elements:
            if (a + b) % m == 0:
                found = True
                break
        if not found:
            return False
    return True


# Step 6: Check whether the set forms a GROUP under addition modulo m
def check_group(elements, m):
    return (
        check_closure_add(elements, m)
        and check_associativity_add(elements, m)
        and check_identity_add(elements, m)
        and check_inverse_add(elements, m)
    )


# Step 7: Check whether the set forms a RING modulo m
def check_ring(elements, m):
    # Must be a group under addition
    if not check_group(elements, m):
        return False

    # Must be closed under multiplication
    if not check_closure_mul(elements, m):
        return False

    # Step 8: Check distributive laws
    for a in elements:
        for b in elements:
            for c in elements:
                # Left distributive law
                if (a * (b + c)) % m != (a * b + a * c) % m:
                    return False
                # Right distributive law
                if ((a + b) * c) % m != (a * c + b * c) % m:
                    return False
    return True


# Step 9: Check whether the set forms a FIELD modulo m
def check_field(elements, m):
    # Must be a ring
    if not check_ring(elements, m):
        return False

    # Multiplicative identity (1) must exist
    if 1 not in elements:
        return False

    # Step 10: Check multiplicative inverse for every non-zero element
    for a in elements:
        if a != 0:
            found = False
            for b in elements:
                if (a * b) % m == 1:
                    found = True
                    break
            if not found:
                return False
    return True


# Step 11: Find modular inverse of an element
def modular_inverse(a, elements, m):
    for b in elements:
        if (a * b) % m == 1:
            return b
    return None


# Step 12: Perform modular division in a field
def modular_division(a, b, elements, m):
    if b == 0:
        raise ValueError("Division by zero is not defined in a field")
    inv = modular_inverse(b, elements, m)
    if inv is None:
        raise ValueError("No modular inverse exists")
    return (a * inv) % m


# =====================================================
# Step 13: Main Program (Menu Driven)
# =====================================================

print("1. Check GROUP")
print("2. Check RING")
print("3. Check FIELD")

choice = int(input("Enter your choice (1-3): "))
m = int(input("Enter modulus m: "))

# Step 14: Automatically generate elements of Z_m
elements = list(range(m))
print("Elements considered:", elements)

# Step 15: Perform selected operation
if choice == 1:
    print("\nChecking GROUP...")
    print("GROUP" if check_group(elements, m) else "NOT a GROUP")

elif choice == 2:
    print("\nChecking RING...")
    print("RING" if check_ring(elements, m) else "NOT a RING")

elif choice == 3:
    print("\nChecking FIELD...")
    if check_field(elements, m):
        print("FIELD")

        # Step 16: Modular division is allowed only in a field
        ch = input("Do you want to perform modular division? (y/n): ").lower()
        if ch == 'y':
            a = int(input("Enter dividend a: "))
            b = int(input("Enter divisor b (non-zero): "))
            try:
                result = modular_division(a, b, elements, m)
                print(f"{a} / {b} (mod {m}) = {result}")
            except ValueError as e:
                print(e)
    else:
        print("NOT a FIELD")

else:
    print("Invalid choice")

#OUTPUT:
1. Check GROUP
2. Check RING
3. Check FIELD
Enter your choice (1-3): 3
Enter modulus m: 6
Elements considered: [0, 1, 2, 3, 4, 5]

Checking FIELD...
NOT a FIELD
