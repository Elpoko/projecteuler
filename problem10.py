#  problem 1
# sum = 0
# for i in range(1, 1000):
    # if i % 3 == 0 or i % 5 == 0:
        # sum += i
# print(sum)

# problem 2
# f0 = 1
# f1 = 2
# sum = 0
# while f1 < 4000000:
    # if f1 % 2 ==0:
        # sum += f1
    # f1 = f1 + f0
    # f0 = f1 - f0
# print(sum)

# problem 3
#p = 600851475143
#i = 2
#while i * i < p:
#    if p % i ==0:
#        p = p / i
#    else:
#        i = i + 1
#print(p)

# problem 4
#a = 999
#max = 0
#while a > 99:
#    b = 999
#    while b > 99:
#        c = a * b
#        if c > max and (str(c) == str(c)[::-1]):
#            max = c
#        print(c)
#        b -= 1
#    a -= 1
#print(max)

# problem 5
# m = 1
# p = [5, 7, 9, 11, 13, 16, 17, 19]
# for i in p:
#     m = m * i

# for i in range(1,21):
#     if m % i == 0:
#         print(i)

# problem 6
# s = 0
# for i in range(1,101):
#     for j in range(1, 101):
#         if i == j:
#             continue
#         else:
#             s += i * j
# print(s)

# problem 7
# p = [2, 3, 5, 7, 11, 13, 17, 19]
# m = 21
# while len(p) < 10001:
#     c = True
#     for i in p:
#         if m % i == 0:
#             c = False
#             break
#     if c:
#         p.append(m)
#     m += 2
# print(p)
# print(len(p))

# problem 8
# d = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# nums = [int(x) for x in str(d)]
# print(nums)
# p = 0
# for i in range(0, len(nums) - 13):
#     q = 1
#     for j in range(i, i+13):
#         q *= nums[j]
#     if p < q:
#         p = q
#         print(nums[i:i+13])
# print(p)

# problem 9
# for i in range(1, 999):
#     for j in range(1, 1000 - i):
#         k = 1000 - i - j
#         if i * i + j * j == k * k:
#             print(i, j, k)
#             print(k*k)
#             print(i * j * k)

# problem 10
# s = 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19
# p = [2, 3, 5, 7, 11, 13, 17, 19]
# for i in range(20, 2000000):
#     c = True
#     if i not in p:
#         for j in p:
#             if i % j == 0:
#                 c = False
#                 break
#     if c:
#         p.append(i)
#         s += i
#         print(i)
# print(p)

# from time import time
# # 175 ms for all the primes up to the value 10**6
# def primes_sieve(limit):
#     a = [True] * limit
#     a[0] = a[1] = False
#     a[2] = True
#     for n in range(4, limit, 2):
#         a[n] = False
#     root_limit = int(limit**.5)+1
#     for i in range(3,root_limit):
#         if a[i]:
#             for n in range(i*i, limit, 2*i):
#                 a[n] = False
#     return a

# LIMIT = 2*10**6
# primes = primes_sieve(LIMIT)
# print(primes)

# s = 0
# for i, n in enumerate(primes):
#     if n:
#         print(i)
#         s += i
# print(s)