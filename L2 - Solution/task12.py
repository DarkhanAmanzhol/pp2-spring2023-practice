n: int = int(input())
arr: list = []

for i in range(n):
    pair: list = input().split(' ')
    key, value = pair[0], pair[1]

    if key == 'str':
        arr.append(value)
    elif key == 'bool':
        arr.sort(reverse=bool(value))
    elif key == 'int':
        index: int = int(value)
        if 0 > index >= len(arr):
            continue

        arr = arr[index:]
    elif key == 'set':
        arr.append(value)
        arr = list(set(arr))
    else:
        arr.insert(0, key)
        arr.append(value)

print(arr)