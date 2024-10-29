from functools import reduce
# a = reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
# print(a)

# a = reduce(lambda x, y: x + y, ["h", "e", "l", "l", "o"])
# print(a)

# return array of length limit containing True or False in each position. primes[i] = true => i is prime
# def eras(limit):
#     primes = [True] * limit
#     primes[0] = False
#     primes[1] = False
#     for i in range(4, limit, 2):
#         primes[i] = False
#     for i in range(3, int(limit**0.5), 2):
#         if primes[i]:
#             for j in range(i*i, limit, 2*i):
#                 primes[j] = False
#     return primes

# limit = 10000
# PRIMES = eras(limit)

def proper_divisors_of_number(x):
    divisors = []
    if x % 2 == 0:
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                divisors.append(i)
                divisors.append(x // i)
    else:
        # if x is odd, no need to check for even divisors, so we only check for odd divisors.
        for i in range(1, int(x**0.5) + 1, 2):
            if x % i == 0:
                divisors.append(i)
                divisors.append(x // i)
    return sorted(set(divisors))

# sum the divisors of a number and return the sum
def sum_of_divisors(x):
    if x == 0: return 0
    return (reduce(lambda x, y: x + y, proper_divisors_of_number(x)) - x)

# check if x and y are amicable numbers. Do the proper divisors of x sum to y, and the proper divisors of y sum to x?
# return True or False
def numbers_are_amicable(x, y):
    sum_x = sum_of_divisors(x)
    sum_y = sum_of_divisors(y)
    if sum_x == y and sum_y == x:
        return True
    else:
        return False

print(numbers_are_amicable(220, 284))

divisor_sums = [None] * 10000
for i in range(10000):
    divisor_sums[i] = sum_of_divisors(i)

def get_indices_in_divisor_sums(x):
    global divisor_sums
    if x in divisor_sums:
        indices = []
        for i, n in enumerate(divisor_sums):
            if n == x:
                indices.append(i)
        return indices
    else:
        return False
"""    
amicables = set()
for i in set(divisor_sums):
    if i < 10000:
        possible_amicable_numbers = get_indices_in_divisor_sums(i)
        for j in possible_amicable_numbers:
            if numbers_are_amicable(i, j) and (i != j):
                # print("amicable: ", i, j)
                amicables.add(i)
                amicables.add(j)
print('amicables', amicables)
print('sum of amicables', sum(amicables))
"""

# shorter approach, using relation d(d(a)) = a for amicable numbers
def factors_sum(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return sum(factors) + 1

a_sum = 0
for i in range(10000):
    if factors_sum(factors_sum(i)) == i:
        if factors_sum(i) != i:
            print(i)
            a_sum += i
print(a_sum) 