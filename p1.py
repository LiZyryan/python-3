def sum_even_indexes_and_multiply(lst):
    if not lst:
        return 0
    even_index_sum = sum(lst[::2])
    return even_index_sum * lst[-1]

# Перевірка прикладів
print(sum_even_indexes_and_multiply([0, 1, 7, 2, 4, 8]))  
print(sum_even_indexes_and_multiply([1, 3, 5]))
print(sum_even_indexes_and_multiply([6]))
print(sum_even_indexes_and_multiply([]))
