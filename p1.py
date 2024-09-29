def split_list(lst):
    if not lst:
        return [[], []]
    mid = (len(lst) + 1) // 2
    fst_part = lst[:mid]
    sec_part = lst[mid:]
    return [fst_part, sec_part]
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))