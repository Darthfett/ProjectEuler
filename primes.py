from collections import Counter

primes = [2, 3]

def gen_next_prime():
    maybe_prime = primes[-1] + 2
    while any(maybe_prime % prime == 0 for prime in primes):
        maybe_prime = maybe_prime + 2

    primes.append(maybe_prime)


def prime_numbers():
    i = 0
    while True:
        if i == len(primes):
            gen_next_prime()
        assert i < len(primes)
        yield primes[i]
        i += 1


def is_prime(i):
    while primes[-1] ** 2 < i:
        gen_next_prime()

    for prime in primes:
        if prime ** 2 > abs(i):
            return True
        if i % prime == 0:
            return False
    return True

def factor_primes(i):
    prime_factors = Counter()
    while not is_prime(i):
        for prime in primes:
            if i % prime == 0:
                prime_factors[prime] += 1
                i = i // prime
                break
    prime_factors[i] += 1
    return prime_factors