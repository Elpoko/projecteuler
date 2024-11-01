def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# help from nmadnani
digits = [*range(10)]
answer = []
index = 10**6 - 1 
while len(digits) != 1:
    a = factorial(len(digits) - 1)
    dig = digits[index // a]
    answer.append(dig)
    index = index % a
    digits.remove(dig)
answer.append(digits[0])
print(answer)

# divisions = [0] * 10
# rem = 10**6
# for i in range(9, 0, -1):
#     div = rem // factorial(i)
#     print(i, rem // factorial(i), rem - div*factorial(i))
#     rem = rem - div * factorial(i)
# for i in range(10, 0, -1):
#     divisions[i-1] = rem // factorial(i)
#     rem = rem % factorial(i)
# print(divisions)


# permutations = []
# for i_0 in range(10):
#     for i_1 in [x for x in digits if x != i_0]:
#         for i_2 in [x for x in digits if x not in [i_0, i_1]]:
#             for i_3 in [x for x in digits if x not in [i_0, i_1, i_2]]:
#                 for i_4 in [x for x in digits if x not in [i_0, i_1, i_2, i_3]]:
#                     for i_5 in [x for x in digits if x not in [i_0, i_1, i_2, i_3, i_4]]:
#                         for i_6 in [x for x in digits if x not in [i_0, i_1, i_2, i_3, i_4, i_5]]:
#                             for i_7 in [x for x in digits if x not in [i_0, i_1, i_2, i_3, i_4, i_5, i_6]]:
#                                 for i_8 in [x for x in digits if x not in [i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7]]:
#                                     for i_9 in [x for x in digits if x not in [i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8]]:
#                                         permutations.append([i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9])

# print(permutations[999999])




