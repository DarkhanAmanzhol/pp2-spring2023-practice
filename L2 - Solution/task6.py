my_list = [(1,2), (2,3), (3,7), (4,16)] # list of tuples

results = [] # collects all the results
for num1, num2 in my_list: # can be used tuple and list most of the time for this type of operation.
    results.append(num1 + num2) # array method to add value to the list.

print(results)