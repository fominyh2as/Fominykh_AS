# TODO Найдите количество книг, которое можно разместить на дискете

disk_capacity_mb = 1.44            # Объем дискеты в Мб
pages_in_book = 100                 # Количество страниц в книге
lines_per_page = 50                 # Количество строк на странице
chars_per_line = 25                 # Количество символов в строке
bytes_per_char = 4                  # Количество байт на один символ

# Перевод объема дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

# Рассчитываем объем одной книги
book_size_bytes = (pages_in_book * lines_per_page * chars_per_line * bytes_per_char)

# Рассчитываем, сколько книг поместится на дискету
number_of_books = disk_capacity_bytes // book_size_bytes
print("Количество книг, помещающихся на дискету:",int(number_of_books))
