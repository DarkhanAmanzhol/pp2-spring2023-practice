def count_integer(list1):
    els = list(map(lambda i: isinstance(i, float), list1)) 
    result = len([e for e in els if e])         
    return result
    
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(count_integer(list1))