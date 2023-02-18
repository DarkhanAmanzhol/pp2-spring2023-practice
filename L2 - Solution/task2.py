#  Set -> pop, discard, remove
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]

s = set(a) # Removes all duplicates automatically

query = int(input()) # from input comes string, if this is number or anything else than string, please convert it!!! In this case integer => int()

for _ in range(query): # _ is shows that you won’t use index value! Can be value.
    q = tuple(input().split()) # tuple or list can be used.Example(‘pop’,)
    if q[0] == "pop": # (‘pop,) => first element is ‘pop’ (q[0]) == ‘pop’
        s.pop() # Then activates this line of condition
    elif q[0] == "discard":
        s.discard(int(q[1]))
    elif q[0] == "remove":
        s.remove(int(q[1]))

print(sum(s)) # This function pluses all values in the list.
