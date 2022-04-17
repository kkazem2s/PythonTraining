def get_name():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    print_swapped_name(firstname, lastname)


def print_swapped_name(firstname, lastname):
    print(lastname + " " + firstname)


get_name()
