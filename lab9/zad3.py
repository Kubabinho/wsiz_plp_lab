import math

def solve_quadratic():
    """
    Program do rozwiązania równania kwadratowego przy użyciu formuły kwadratowej.
    Równanie kwadratowe ma postać: ax^2 + bx + c = 0
    """
    print("\n--- Rozwiązywanie równania kwadratowego ---")
    try:
        a = float(input("Podaj współczynnik a: "))
        if a == 0:
            print("Współczynnik 'a' nie może być równy zero w równaniu kwadratowym.")
            return

        b = float(input("Podaj współczynnik b: "))
        c = float(input("Podaj współczynnik c: "))

        # Oblicz deltę (b^2 - 4ac)
        delta = b**2 - 4*a*c

        if delta > 0:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"Równanie ma dwa pierwiastki rzeczywiste: x1 = {root1}, x2 = {root2}")
        elif delta == 0:
            root = -b / (2 * a)
            print(f"Równanie ma jeden podwójny pierwiastek rzeczywisty: x = {root}")
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-delta) / (2 * a)
            print(f"Równanie ma dwa pierwiastki zespolone: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

    except ValueError:
        print("Błąd: Podano nieprawidłowe dane. Upewnij się, że wprowadzasz liczby.")

if __name__ == "__main__":
    solve_quadratic()
