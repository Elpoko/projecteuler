def triangle_number(n):
    return (n * (n+1)) // 2

def eras(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i in range(2, limit, 2):
        primes[i] = False
    for i in range(3, limit):
        if primes[i]:
            for j in range(i*i, limit, 2*i):
                primes[j] = False
    return primes

def factors(n):
    if n == 1:
        return set([1])
    elif primes[n]:
        return set([1, n])
    else:
        factors = set([1, n])
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        return sorted(factors)

primes = eras(10**8)

for i in range(1, 10**5):
    print(i, len(factors(triangle_number(i))))
    if len(factors(triangle_number(i))) > 500:
        print(i, triangle_number(i), len(factors(triangle_number(i))))
        break