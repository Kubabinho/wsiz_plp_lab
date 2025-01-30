class Prostokat:
    """
    Klasa reprezentująca prostokąt z polami długość i szerokość.
    Umożliwia obliczanie pola i obwodu prostokąta.
    """
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def oblicz_pole(self):
        """Oblicza pole prostokąta."""
        return self.dlugosc * self.szerokosc

    def oblicz_obwod(self):
        """Oblicza obwód prostokąta."""
        return 2 * (self.dlugosc + self.szerokosc)

if __name__ == "__main__":
    dlugosc = float(input("Podaj długość prostokąta: "))
    szerokosc = float(input("Podaj szerokość prostokąta: "))

    prostokat = Prostokat(dlugosc, szerokosc)

    print(f"Pole prostokąta: {prostokat.oblicz_pole()}")
    print(f"Obwód prostokąta: {prostokat.oblicz_obwod()}")
