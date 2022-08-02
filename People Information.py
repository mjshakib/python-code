import os
choice=''

extension = ".txt"
command = ''
while command not in [1, 2]:

    command = input('Enter 1 for read or 2 for write: ')

    if command == '1':
        # Taking name from user
        name = input('Enter your name: ')
        if not name:
            continue

        filename = "_".join(name.lower().split(' '))  # Replacing space to lodash and doing lower case

        # Making absolute path
        full_filename = filename + extension
        absolute_path = os.path.join(os.getcwd(), full_filename)
        is_file_exist = os.path.isfile(absolute_path)

        # Searching file and printing
        if is_file_exist:
            file = open('{0}'.format(absolute_path), "r")
            name = file.readline()
            age = file.readline()
            gender = file.readline()
            profession = file.readline()
            print(' Name= {0} Age={1} Gender={2} Profession={3}'.format(name, age, gender, profession))

            file.close()
        else:
            print('Name {} not found at path '.format(name))
            print(absolute_path)
            # break

    if command == '2':
        # Taking user information
        name = input('Please enter your name: ')
        age = input('Age: ')
        gender = input('Gender: ')
        profession = input('Profession: ')

        # Making absolute path
        file_name = "_".join(name.lower().split(' '))
        full_filename = file_name + extension
        absolute_path = os.path.join(os.getcwd(), full_filename)

        # Saving information to file
        file = open(absolute_path, "w")
        name_line = "\n"
        file.write(name + name_line)
        file.write(age + name_line)
        file.write(gender + name_line)
        file.write(profession + name_line)
        file.close()
