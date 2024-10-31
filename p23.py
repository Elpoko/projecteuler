def check_if_abundant(n):
    sum_of_factors = sum(x + (n / x) for x in range(2, int(n**0.5) + 1) if n % x == 0) + 1
    if (n**0.5) % 1 == 0:
        sum_of_factors -= n**0.5
    return sum_of_factors > n
        # return True
    # else:
        # return False
    
# abundant_numbers = [n for n in range(1, 28124) if check_if_abundant(n)]
# is_abundant_sum = [False] * 28124
# # [is_abundant_sum[2*i] = True for i in abundant_numbers and i < 14062]
# for pos_i, i in enumerate(abundant_numbers):
#     for j in abundant_numbers[pos_i:]:
#         if i + j < 28124:
#             is_abundant_sum[i+j] = True

# for i in range(1, 28124):
#     if check_if_abundant(i):
#         abundant_numbers.append(i)
        # for j in abundant_numbers:
        #     if (i + j) < 28124:
        #         abundant_numbers_sums.append(int(i+j))

# for i in abundant_numbers:
#     for j in abundant_numbers:
#         if (i+j) < 28124:
#             is_abundant_sum[i+j] = True

# total = 0
# for num, is_sum in enumerate(is_abundant_sum):
#     if is_sum == False:
#         total += num
# print(total)
ANSWER = 4179871

# quick version, ini
def problem_23(N=28123):
    N = min(N, 28123)
    proper_divisor_sum = [0] * N
    for i in range(1, N):
        for j in range(2*i, N, i):
            proper_divisor_sum[j] += i
    is_abundant = lambda n: (n > 0 and proper_divisor_sum[n] > n)
    abundant_numbers = [n for n in range(12, N) if is_abundant(n)]
    abundant_numbers = {
        i: [ n for n in abundant_numbers if n % 6 == i]
        for i in range(6)
    }
    abundant_sums = {
        *range(12 + min(abundant_numbers[0]), N, 6),
        *range(12 + min(abundant_numbers[2]), N, 6),
        *range(12 + min(abundant_numbers[3]), N, 6),
        *range(12 + min(abundant_numbers[4]), N, 6),
        *([40] if N > 40 else [])
    }

    for n in range(N):
        if n % 6 == 1 or n % 6 == 5:
            if any(is_abundant(n - a) for a in abundant_numbers[3]):
                abundant_sums.add(n)

    return sum(n for n in range(N) if n not in abundant_sums)

r = problem_23()
print(r)
# fast!