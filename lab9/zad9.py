def permutacje(lst):
    if len(lst) == 0:
        return [[]]  # Jedyna "permutacja" pustej listy to lista pusta
    if len(lst) == 1:
        return [lst]  # Jedyna "permutacja" listy z jednym elementem to sama lista

    perm_list = []
    for i in range(len(lst)):
        elem = lst[i]
        remaining = lst[:i] + lst[i + 1:]  # Utworzenie nowej listy bez elementu lst[i]

        for p in permutacje(remaining):  # Rekurencyjnie permutacja pozostałych elementów
            perm_list.append([elem] + p)  # Dodanie elem do każdej permutacji pozostałych

    return perm_list


# Przykład użycia
numbers = [1, 2, 3]
permutations = permutacje(numbers)

# Drukowanie permutacji
for p in permutations:
    print(p)
