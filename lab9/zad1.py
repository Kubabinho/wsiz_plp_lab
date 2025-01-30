def sum_of_digits():
    """
    Funkcja obliczająca sumę cyfr liczby podanej przez użytkownika.
    """
    try:
        number = input("Podaj liczbę: ")
        digit_sum = sum(int(digit) for digit in number if digit.isdigit())
        print(f"Suma cyfr liczby {number} wynosi {digit_sum}.")
    except ValueError:
        print("Podano nieprawidłowe dane. Proszę podać liczbę całkowitą.")

if __name__ == "__main__":
    sum_of_digits()
