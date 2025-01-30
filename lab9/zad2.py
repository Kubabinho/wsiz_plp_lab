def calculator():
    """
    Kalkulator z podstawowymi operacjami matematycznymi: dodawanie, odejmowanie,
    mnożenie i dzielenie.
    """
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Błąd: Dzielenie przez zero."
        return a / b

    while True:
        print("\n--- Kalkulator ---")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjście")

        choice = input("Wybierz operację (1/2/3/4/5): ")

        if choice == "5":
            print("Zamykam kalkulator.")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Podaj pierwszą liczbę: "))
                num2 = float(input("Podaj drugą liczbę: "))

                if choice == "1":
                    print(f"Wynik: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Wynik: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Wynik: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Wynik: {divide(num1, num2)}")

            except ValueError:
                print("Błąd: Podano nieprawidłową liczbę.")
        else:
            print("Błąd: Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    calculator()
