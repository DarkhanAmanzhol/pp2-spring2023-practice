def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number + 1):
        if i * i > number:
            return True

        if number % i == 0:
            return False

def prime_with_prime_index(number: int) -> list:
    numbers = [i for i in range(2, number + 1)]

    primes = list(filter(is_prime, numbers))

    prime_indeces = list(filter(is_prime, range(1, len(primes) + 1)))

    return [primes[i - 1] for i in prime_indeces]

number = int(input())

print(prime_with_prime_index(number))