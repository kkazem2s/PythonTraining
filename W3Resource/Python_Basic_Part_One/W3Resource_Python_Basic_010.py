def calculate(n):
    second_number = str(n) + str(n)
    third_number = second_number + str(n)
    return n + int(second_number) + int(third_number)


print(calculate(5))
