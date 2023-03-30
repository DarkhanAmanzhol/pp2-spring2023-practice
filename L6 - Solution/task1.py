# You are writing some kind of blog for your everyday occasions.
# Write 3 functions which can handle 3 options based on what you need to append/change, create or remove files. No need to validate.
import os

def createFile(fname):
    file = open(fname +'.txt', 'x')
    print('Successfully created file named', file.name)
    file.close()

def readFile(fname):
    file = open(fname +'.txt', 'r')
    print('*******************\n'+file.read()+'\n*******************\n')
    file.close()

def appendFile(fname):
    file = open(fname +'.txt', 'a+')
    file.seek(0)
    print('*******************\n'+file.read()+'\n*******************\n')
    new_text = input(f'Add text above {file.name}:\n')
    file.write('\n\n'+new_text)
    file.close()

def overwriteFile(fname):
    file = open(fname +'.txt', 'w')
    new_text = input(f'Overwrite {file.name} with new text:\n')
    file.write(new_text)
    file.close()

def removeFile(fname):
    if os.path.isfile(fname +'.txt'):
        os.remove(fname +'.txt')
        print('Successfully deleted file named', fname + '.txt')
    else:
        # If it fails, inform the user.
        print(f"Error: {fname} file not found")


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))
file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')