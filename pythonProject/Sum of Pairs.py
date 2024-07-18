
def sum_pairs(ints, sum_value):
    seen = {}
    for i, num in enumerate(ints):
        complement = sum_value - num
        if complement in seen:
            return [complement, num]
        if num not in seen:
            seen[num] = i
    return None




print(sum_pairs([4, 3, 2, 3, 4],6))
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
