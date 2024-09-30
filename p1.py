def zero_to_end(lst):
    non_zero = [num for num in lst if num != 0]
    zero_count = lst.count(0)
    result = non_zero + [0] * zero_count
    return result
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = zero_to_end(lst)
print(result)
