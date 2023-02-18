# Simple iterator example
class CycleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.iterable_obj = 0

    def __next__(self):
        if self.iterable_obj >= self.max_times:
            raise StopIteration
        value = self.data[self.iterable_obj % len(self.data)]
        self.iterable_obj += 1
        return value

class Cycle():

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)

c = Cycle('abc', 5)
# c = Cycle('string', 9)
print(list(c))        # prints a, b, c, a, b