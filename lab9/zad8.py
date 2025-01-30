def fibonacci(n):
    if n <= 0:
        return "Błędny argument, n musi być liczbą naturalną większą od 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Przykładowe wywołanie funkcji
print(fibonacci(7))  # Wynik: 8
