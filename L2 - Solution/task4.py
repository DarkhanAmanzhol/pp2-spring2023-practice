#  Dictionary
s = input()

words = s.split()

counts = {} # Dictionary has ‘key’ and ‘value’, initialization. Same as => counts = dict()
for word in words: # checks each word in the array
    if word not in counts: # If ‘word’ not in the dictionary,then runs this condition
        counts[word] = 1 # Creates new key with 'word' and value with 1.
    else:
        counts[word] += 1 # Otherwise adds one more count to the value where key is equal to 'word'