import datetime


class Example:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.Inner_iter(self.n)

    class Inner_iter:
        def __init__(self, n):
            self.i = 0
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.n:
                i = self.i
                self.i += 1

                return int(i * (i + 1) / 2)
            else:
                raise StopIteration()


    class Reverse_iter:
        def __init__(self, iter):
            self.data = list(iter)
            self.index = len(self.data)

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.index < 1:
                raise StopIteration
            
            self.index -= 1
            return self.data[self.index]


    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def take(n, iterator):
        ret = []
        for i in range(n):
            ret.append(next(iterator))

        return ret

    def get_generator():
        return ((x, y, z) for z in Example.integers() 
                          for y in range(1, z) 
                          for x in range(1, y) 
                          if x ** 2 + y ** 2 == z ** 2)

    def to_day(n, month):
        if month == 2:
            return (n + 27) % 28 + 1
        elif month in [4, 6, 9, 11]:
            return (n + 28) % 30 + 1
        else:
            return n % 31 + 1

    def to_mon(n):
        return (n + 11) % 12 + 1

    def to_year(n):
        return 2000 + n

    def conver_to_dates(arr):
        result = []

        for i in arr:
            year = Example.to_year(i[2])
            mon = Example.to_mon(i[1])
            day = Example.to_day(i[0], mon)

            result.append(datetime.datetime(year=year, month=mon, day=day))

        return result

    def date_in_format(date: datetime.datetime, format=1):
        if format == 1:
            return date.strftime('%d/%m/%Y')
        elif format == 2:
            return date.strftime('%Y-%m-%d')
        elif format == 3:
            return date.strftime('%d %B, %Y')
        else:
            print('unsupported format')
            return None
