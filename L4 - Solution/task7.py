class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def get_fibonacci_numbers(n):
    iterator = FibonacciIterator()
    result = []
    for i in range(n):
        result.append(next(iterator))
    return result

print(get_fibonacci_numbers(5))