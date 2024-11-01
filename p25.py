length = 0
index = 2
a = 1
b = 1
while length < 1000:
    length = len(str(a+b))
    a, b = b, a+b
    index += 1
print(index, length)
answer = 4782

# binet's formula / moskova
import math
phi = 1.618034
num = 999 + 0.5 * math.log10(5)
denom = math.log10(phi)
print(math.ceil(num/denom))
