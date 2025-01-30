import csv

def calculate_column_average(file_path, column_name):
    """
    Funkcja do analizy danych z pliku CSV, która oblicza średnią dla wybranej kolumny.
    :param file_path: Ścieżka do pliku CSV
    :param column_name: Nazwa kolumny, dla której obliczana jest średnia
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            values = []

            for row in reader:
                if column_name in row and row[column_name].strip().isdigit():
                    values.append(float(row[column_name]))

            if values:
                average = sum(values) / len(values)
                print(f"Średnia dla kolumny '{column_name}' wynosi: {average}")
            else:
                print(f"Kolumna '{column_name}' nie zawiera żadnych wartości numerycznych lub nie istnieje.")

    except FileNotFoundError:
        print(f"Błąd: Plik '{file_path}' nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    file_path = input("Podaj ścieżkę do pliku CSV: ")
    column_name = input("Podaj nazwę kolumny: ")
    calculate_column_average(file_path, column_name)
