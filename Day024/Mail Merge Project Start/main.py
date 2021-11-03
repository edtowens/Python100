# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
INVITED_NAME_PATH = "./Input/Names/invited_names.txt"
READY_TO_SEND_PATH = "./Output/ReadyToSend/"
updated_list = []


def get_lines(file_path):
    with open(file_path, "r") as file:
        lines_list = file.readlines()
    return lines_list


def replace_name(name_to_invite):
    contents = get_lines(STARTING_LETTER_PATH)
    new_contents = contents
    new_contents[0] = f"Dear {name_to_invite},\n"
    return new_contents


def create_file(file_path, contents_list, name):
    new_file_path = file_path + name + "_invite.txt"
    with open(new_file_path, "x") as file:
        for line in contents_list:
            file.write(line)


def strip_new_lines(list_of_names):
    new_list = []
    for name_item in list_of_names:
        new_list.append(name_item.strip("\n"))
    return new_list


# replace name in contents with every name to invite
name_list = strip_new_lines(get_lines(INVITED_NAME_PATH))
for name in name_list:
    updated_list.clear()
    updated_list = replace_name(name)
    create_file(READY_TO_SEND_PATH, updated_list, name)
