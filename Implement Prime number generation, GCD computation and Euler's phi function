# Step 1: Function to check whether a number is prime
def is_prime(n):
    # If number is less than 2, it is not prime
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # If number is even and greater than 2, it is not prime
    if n % 2 == 0:
        return False

    # Step 2: Check divisibility only up to square root of n
    # Skip even numbers by checking only odd divisors
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True


# Step 3: Function to generate all prime numbers up to n
def generate_primes(n):
    primes = []

    # Check each number from 2 to n
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes


# Step 4: Function to compute GCD using Euclidean Algorithm
def gcd(a, b):
    # Repeat until remainder becomes zero
    while b != 0:
        a, b = b, a % b

    # When b is zero, a contains the GCD
    return a


# Step 5: Function to compute Euler's Totient Function
def euler_phi(n):
    result = n
    temp = n

    # Step 6: Check for prime factor 2
    if temp % 2 == 0:
        result -= result // 2
        while temp % 2 == 0:
            temp //= 2

    # Step 7: Check for all odd prime factors
    for i in range(3, int(temp**0.5) + 1, 2):
        if temp % i == 0:
            result -= result // i
            while temp % i == 0:
                temp //= i

    # Step 8: If remaining number is a prime factor greater than 1
    if temp > 1:
        result -= result // temp

    return result


# Step 9: Read input and generate prime numbers
n = int(input("Enter a number to generate prime numbers up to n: "))
print("Prime numbers:", generate_primes(n))

# Step 10: Read input values and compute GCD
a = int(input("\nEnter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print("GCD:", gcd(a, b))

# Step 11: Read input and compute Euler's Totient value
num = int(input("\nEnter a number to find Euler's Phi value: "))
print("Euler's Phi value:", euler_phi(num))

#OUTPUT:
Enter a number to generate prime numbers up to n: 10
Prime numbers: [2, 3, 5, 7]

Enter first number for GCD: 78
Enter second number for GCD: 56
GCD: 2

Enter a number to find Euler's Phi value: 9
Euler's Phi value: 6
