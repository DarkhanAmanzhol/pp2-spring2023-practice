arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktay"]
only_ints = []
list_of_string = []
float_nums = []
array_of_bools = []

for element in arr2:
    if type(element) == str:
        list_of_string.append(element)
    elif type(element) == int:
        only_ints.append(element)
    elif type(element) == float:
        float_nums.append(element)
    elif type(element) == bool:
        array_of_bools.append(element)
print(only_ints)
print(list_of_string)
print(float_nums)
print(array_of_bools)