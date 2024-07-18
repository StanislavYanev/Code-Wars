def square_digits(num):
    num_list = list(str(num))
    ints  = ''
    for number in num_list:
        value = int(number)*int(number)
        ints += str(value)
    return int(ints)


print(square_digits(9119))