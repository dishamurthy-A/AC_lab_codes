print(" DIFFIE–HELLMAN KEY EXCHANGE SIMULATION")

# Step 1: Public parameters
p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

print("\nSTEP 1: Choose Public Parameters")
print(f"Prime number (p) = {p}")
print(f"Generator (g) = {g}")

# Step 2: Alice selects private key
a = int(input("Enter Alice's private key (a): "))
A = (g ** a) % p

print("\nSTEP 2: Alice Selects Private Key")
print(f"Alice private key (a) = {a}")
print(f"Alice computes public key:")
print(f"A = g^a mod p")
print(f"A = {g}^{a} mod {p}")
print(f"A = {A}")

# Step 3: Bob selects private key
b = int(input("Enter Bob's private key (b): "))
B = (g ** b) % p

print("\nSTEP 3: Bob Selects Private Key")
print(f"Bob private key (b) = {b}")
print(f"Bob computes public key:")
print(f"B = g^b mod p")
print(f"B = {g}^{b} mod {p}")
print(f"B = {B}")

# Step 4: Exchange public keys
print("\nSTEP 4: Exchange Public Keys Over Insecure Channel")
print(f"Alice sends A = {A} to Bob")
print(f"Bob sends B = {B} to Alice")
print("(Attacker can see A and B, but not a and b)")

# Step 5: Compute shared secret
alice_secret = (B ** a) % p
bob_secret = (A ** b) % p

print("\nSTEP 5: Compute Shared Secret")
print("Alice computes:")
print(f"S = B^a mod p")
print(f"S = {B}^{a} mod {p}")
print(f"S = {alice_secret}")

print("\nBob computes:")
print(f"S = A^b mod p")
print(f"S = {A}^{b} mod {p}")
print(f"S = {bob_secret}")

# Step 6: Verify shared secrets
print("\nSTEP 6: Verify Shared Secret")
if alice_secret == bob_secret:
    print("Shared secrets match ✔")
    print("Secure Session Key Established!")
else:
    print("Shared secrets do NOT match")

#OUTPUT:
 DIFFIE–HELLMAN KEY EXCHANGE SIMULATION
Enter prime number (p): 47
Enter generator (g): 3

STEP 1: Choose Public Parameters
Prime number (p) = 47
Generator (g) = 3
Enter Alice's private key (a): 7

STEP 2: Alice Selects Private Key
Alice private key (a) = 7
Alice computes public key:
A = g^a mod p
A = 3^7 mod 47
A = 25
Enter Bob's private key (b): 13

STEP 3: Bob Selects Private Key
Bob private key (b) = 13
Bob computes public key:
B = g^b mod p
B = 3^13 mod 47
B = 36

STEP 4: Exchange Public Keys Over Insecure Channel
Alice sends A = 25 to Bob
Bob sends B = 36 to Alice
(Attacker can see A and B, but not a and b)

STEP 5: Compute Shared Secret
Alice computes:
S = B^a mod p
S = 36^7 mod 47
S = 16

Bob computes:
S = A^b mod p
S = 25^13 mod 47
S = 16

STEP 6: Verify Shared Secret
Shared secrets match 
Secure Session Key Established!
