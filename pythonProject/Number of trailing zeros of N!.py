def zeros(n):
    zero_counter = 0
    while n >= 5:
        n //= 5
        zero_counter += n
    return zero_counter


print(zeros(1000000))