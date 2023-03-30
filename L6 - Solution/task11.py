def get_lines(filename: str) -> list:
    if not filename.endswith('.txt'):
        raise ValueError

    try:
        with open(file=filename, mode='r', encoding='UTF-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def get_dictionary(lines: list) -> dict:
    return dict(map(lambda x: (x.split()[0], float(x.split()[1])), lines))

def get_value(dict: dict, name: str) -> float:
    if name in dict.keys():
        return dict[name]

    return -1

def main() -> None:
    file_names = ['2000.txt', '2001.txt', '2002.txt']

    files = input('type file names separeted by space or press enter for all: ')

    if files:
        file_names = files.split(' ')

    name = input('name: ')

    li = map(lambda x: get_value(dict=x, name=name), map(get_dictionary, map(get_lines, file_names)))

    print(max(li))


if __name__ == '__main__':
    main()