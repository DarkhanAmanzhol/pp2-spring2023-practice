import os, sys

os.chdir("C:\\")
while True:
    main_path = os.getcwd()
    input_data = input(f"{main_path} >> ")
    command = input_data.split(maxsplit=1)[0]

    if command == 'q':
        sys.exit(0)
        # break

    path = "".join(input_data.split(maxsplit=1)[1:])

    if command in ("ls", "dir"):
        print(os.listdir(main_path))

    if command == "cd":
        try:
            folders = path.split("\\")

            for folder in folders:
                if folder == "..":
                    main_path = os.path.abspath('..')
                else:
                    main_path = f"{main_path}\\{folder}"

                os.chdir(f"{main_path}\\")

        except FileNotFoundError:
            print("Path is incorrect")

    if command == "cat":
        try:
            f = open(f"{main_path}\\{path}", 'r')
            print(f.read())
            f.close()
        except OSError:
            print('Failed reading the file')

    if command == "mkdir":
        os.mkdir(f"{main_path}\\{path}")

    if command == "rm":
        try:
            if os.path.exists(f"{main_path}\\{path}") and os.path.isfile(f"{main_path}\\{path}"):
                os.remove(path)
                print('File successfully deleted')
            else:
                print('File does not exist')
        except OSError:
            print('Error deleting a file')

    if command == "rmdir":
        try:
            if os.path.exists(f"{main_path}\\{path}") and os.path.isdir(f"{main_path}\\{path}"):
                os.rmdir(f"{main_path}\\{path}")
                print('Directory successfully deleted')
            else:
                print('Incorrect path')
        except OSError:
            print('Error deleting a diractory')