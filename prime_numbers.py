# Jennie Rose Paitan
# Task: Display all the prime numbers between 1 to 250.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    print("Prime numbers between 1 and 250:")
    for num in range(1, 251):
        if is_prime(num):
            print(num, end=" ")

primes()
