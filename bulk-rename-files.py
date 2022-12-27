import os


def rename_files(sub_string, replace_string):
    for root, dirs, files in os.walk("."):
        for file in files:
            old_name = os.path.join(root, file)
            new_name = get_new_name(old_name, sub_string, replace_string)

            # Replacing only if a valid name change
            if new_name == "":
                print(f"Did you just try to remove the entirety of: {old_name} !!!")
            elif new_name != old_name:
                print(f"{old_name} -> {new_name}")
                os.rename(old_name, new_name)


def get_new_name(old_name, sub_string, replace_string):
    # Traversing through the entire name. Using while loop because we're changing the string each [valid] time
    i = 0
    while i < len(old_name) - len(sub_string) + 1:
        if old_name[i] == sub_string[0]:
            # Vars to keep track of the indexes
            begin = i
            end = i

            # Found the name! Let's traverse further to find if it is present in its entirety
            for j in range(1, len(sub_string)):
                if old_name[i + j] != sub_string[j]:
                    end = -1
                    break
                else:
                    end += 1

            # end == -1 indicates that the string was not present in its entirety
            if end != -1:
                old_name = old_name[:begin] + replace_string + old_name[end + 1:]

        i += 1

    # if the entire name is "", just return that (will not be renamed)
    if old_name == [""]:
        return ""

    # Finally returning the name
    return old_name


def init():
    print("** KEEP BACKUPS! **\n")
    sub_string = input("Enter the substring to be removed from the file names in this folder and subdirectories: ")

    if sub_string == "":
        print("You entered nothing?!")
    else:
        replace_string = input("Enter the string to be replaced it with (Just press ENTER if nothing): ")

        print("----- BEGIN PROCESSING -----\n")
        rename_files(sub_string, replace_string)
        print("\n----- END PROCESSING ----- ")


# Self start
init()
