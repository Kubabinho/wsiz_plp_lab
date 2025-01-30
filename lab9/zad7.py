from functools import reduce

# Lista liczb do przetworzenia
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Znajdowanie liczb parzystych
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Suma tych liczb parzystych
sum_even_numbers = reduce(lambda a, b: a + b, even_numbers)

print("Lista liczb parzystych:", even_numbers)
print("Suma liczb parzystych:", sum_even_numbers)