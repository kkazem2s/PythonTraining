def separate_numbers():
    numbers = input("Please enter Numbers seperated by comma: \n")
    numbers_list = numbers.split(",")
    numbers_tuple = tuple(numbers_list)
    print("List: " + str(numbers_list))
    print("Tuple: " + str(numbers_tuple))


separate_numbers()
