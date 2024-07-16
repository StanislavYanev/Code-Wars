# def sum_of_intervals(intervals):
#     intervals.sort(key=lambda x: (x[0], x[1]))
#     marge_intervals = []
#     current_start, current_end = intervals[0]
#     for start, end in intervals[1:]:
#         if start <= current_end:
#             current_end = max(current_end, end)
#         else:
#             marge_intervals.append((current_start, current_end))
#             current_start, current_end = start, end
#     marge_intervals.append((current_start, current_end))
#     total_sum = sum(end - start for start, end in marge_intervals)
#     return total_sum
#

def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a, b in sorted(intervals):
        if top < a:
            top = a
        if top < b:
            s, top = s + b - top, b
    return s


print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
