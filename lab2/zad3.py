def analyze_data(data):
    numbers = filter(lambda x: isinstance(x, (int, float)), data)
    max_number = max(numbers, default=None)

    strings = filter(lambda x: isinstance(x, str), data)
    longest_string = max(strings, key=len, default=None)

    tuples = filter(lambda x: isinstance(x, tuple), data)
    largest_tuple = max(tuples, key=len, default=None)

    return {
        "max_number": max_number,
        "longest_string": longest_string,
        "largest_tuple": largest_tuple
    }

data = [
    42, "siema", (1, 2, 3), [4, 5], {"key": "value"},
    3.14, "elo", (1, 2), "zajecia", 100
]

result = analyze_data(data)
print("Wynik", result)
