# Loop
n = int(input())

i = 1 # Initialization of ‘i’
while True: # Condition is True, then loop runs infinitely
    if i * i > n: # if ‘i * i’ more than the given ‘n’, our condition runs
        break # breaks the loop
    print(i * i, end=" ") # ‘end’ is used to add any string.In this case used “ ”
    i += 1 # Don’t forget this line! Otherwise your code will run forever.
    # This same as i = i + 1 
