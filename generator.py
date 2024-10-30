class first_n():
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        raise StopIteration()
    
# a = first_n(100)
# print(sum(a))

class letter_iter():
    def __init__(self, letter, max):
        self.letter = letter
        self.max = max
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max:
            raise StopIteration()
        cur, self.letter = self.letter, (self.letter + self.letter)
        self.count += 1
        print('count: ', self.count)
        return cur

# b = letter_iter('a', 5)
# for c in b:
#     print(c)

# implement generator
def firstn(n):
    num = 1
    while num <= n:
        yield num
        num += 1
    
# a = firstn(20)
# for a in a:
#     print(a)

doubles = [2 * n for n in range(50)]
print(doubles)
doubles = list(2*n for n in range(50))
print(doubles)