def check_if_abundant(n):
    count = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            count += i
            if i*i != n:
                count += (n // i)
    if count > n:
        return True
    else:
        return False
    
abundant_numbers = []
non_abundant_numbers = []

for i in range(28123):
    if check_if_abundant(i):
        abundant_numbers.append(i)
    else:
        non_abundant_numbers.append(i)

print(abundant_numbers[:1000])
print(non_abundant_numbers[:10])