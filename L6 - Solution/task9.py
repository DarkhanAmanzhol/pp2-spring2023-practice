import os

# Define the input file name and output directory name
input_file = 'input.txt'
output_dir = 'output'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print('Output directory created.')

# Delete the contents of the output directory if it already exists
else:
    for file_name in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file_name)
        os.remove(file_path)
    print('Output directory contents deleted.')

# Open the input file for reading
with open(input_file, 'r') as input_file_obj:

    # Read the content of the input file
    input_content = input_file_obj.read()

    # Write the uppercase version of the input file content to output file 1
    with open(os.path.join(output_dir, 'output1.txt'), 'w') as output_file1_obj:
        output_file1_obj.write(input_content.upper())
        print('Output file 1 created.')

    # Write the lowercase version of the input file content to output file 2
    with open(os.path.join(output_dir, 'output2.txt'), 'w') as output_file2_obj:
        output_file2_obj.write(input_content.lower())
        print('Output file 2 created.')