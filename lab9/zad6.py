class Pojazd:
    """
    Klasa bazowa reprezentująca pojazd.
    """
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def informacje(self):
        """Zwraca informacje o pojeździe."""
        return f"Pojazd: {self.marka} {self.model}"

class Samochod(Pojazd):
    """
    Klasa reprezentująca samochód, dziedziczy po klasie Pojazd.
    """
    def __init__(self, marka, model, liczba_drzwi):
        super().__init__(marka, model)
        self.liczba_drzwi = liczba_drzwi

    def jazda(self):
        """Symuluje jazdę samochodu."""
        return f"Samochód {self.marka} {self.model} jest w ruchu."

    def informacje(self):
        """Zwraca szczegółowe informacje o samochodzie."""
        return f"Samochód: {self.marka} {self.model}, liczba drzwi: {self.liczba_drzwi}"

if __name__ == "__main__":
    marka = input("Podaj markę samochodu: ")
    model = input("Podaj model samochodu: ")
    liczba_drzwi = int(input("Podaj liczbę drzwi samochodu: "))

    samochod = Samochod(marka, model, liczba_drzwi)

    print(samochod.informacje())
    print(samochod.jazda())
