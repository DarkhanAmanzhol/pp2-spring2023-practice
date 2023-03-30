import os

def find_largest_file(directory):
    largest_file = None
    largest_size = -1
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filesize = os.path.getsize(filepath)
            if filesize > largest_size:
                largest_file = filepath
                largest_size = filesize
    return largest_file, largest_size

if __name__ == '__main__':
    directory = input('Enter directory: ')
    largest_file, largest_size = find_largest_file(directory)
    print(f'Largest file: {largest_file} ({largest_size} bytes)')