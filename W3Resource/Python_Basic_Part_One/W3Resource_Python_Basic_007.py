def print_filename():
    filename = input("Please enter a filename: \n")
    print(filename.partition(".")[2])


print_filename()
