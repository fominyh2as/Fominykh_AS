numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

def replace_missing_with_average(numbers):

    missing_index = numbers.index(None)

    filtered_numbers = [num for num in numbers if num is not None]

    average = sum(filtered_numbers) / (len(filtered_numbers) +1)

    numbers[missing_index] = average

    return numbers
print("Измененный список:", replace_missing_with_average(numbers))
