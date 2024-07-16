# def get_larger_numbers(a, b):
#     larger_numbers = []
#     for i in range(len(a)):
#         if a[i] > b[i]:
#             larger_numbers.append(a[i])
#         else:
#             larger_numbers.append(b[i])
#     return larger_numbers


def get_larger_numbers(a, b):
    return [max(x, y) for x, y in zip(a, b)]


arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]

print(get_larger_numbers(arr1, arr2))
