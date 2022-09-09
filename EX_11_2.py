class Pojazd:

    def __init__(self, max_predkosc: int, przebieg: float) -> None:
        self.max_predkosc = max_predkosc
        self.przebieg = przebieg

    def zwieksz_przebieg(self, wartosc: float) -> None:
        self.przebieg += wartosc


def main():
    opel = Pojazd(205, 150_000)
    print("podaj o ile zwiekszyc przebieg: ")
    opel.zwieksz_przebieg(float(input()))
    print("nowy przebieg wynosi " + str(opel.przebieg))


if __name__ == "__main__":
    main()
