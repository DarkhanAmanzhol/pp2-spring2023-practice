class Person:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def sum_money(self):
        return self.fives*5 + self.tens*10 + self.twenties*20

def most_money(wallets):
    st_sum = {}
    for wallet in wallets:
        st_sum[wallet.name] = wallet.sum_money()
    return max(st_sum, key=lambda x:st_sum[x])

john = Person("John", 2, 2, 0)
alice = Person("Alice", 1, 3, 0)
mike = Person("Mike", 0, 0, 2)

print(most_money([john, alice, mike]))
print(most_money([john, alice]))
print(most_money([alice, mike]))