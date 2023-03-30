import os
import shutil

dir_path = input("Enter the directory path: ")

subdirs = { }

for file_name in os.listdir(dir_path):
    file_ext = os.path.splitext(file_name)[1]

    if not file_ext in subdirs:
        subdirs.update({file_ext: file_ext.removeprefix('.')})

    if file_ext in subdirs:
        subdir_name = subdirs[file_ext]

        subdir_path = os.path.join(dir_path, subdir_name)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

        file_path = os.path.join(dir_path, file_name)
        new_file_path = os.path.join(subdir_path, file_name)
        shutil.move(file_path, new_file_path)

print("Files have been organized successfully.")