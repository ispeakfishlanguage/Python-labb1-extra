def even_number_counter(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


print(even_number_counter([2, 1, 2, 3, 4]))  # 3
print(even_number_counter([2, 2, 0]))  # 3
print(even_number_counter([1, 3, 5]))  # 0