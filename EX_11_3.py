#Stwórz klasę reprezentującą Prostokąt.
#Dodaj do niej metody obliczające pole i obwód z przechowywanych pól - szerokości i długości.

class Prostokat:

    def __init__(self, szerokosc, dlugosc):
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc

    def pole(self):
        return self.szerokosc * self.dlugosc

    def obwod(self):
        return 2 * (self.szerokosc + self.dlugosc)

def main():
    prostokat1 = Prostokat(23, 124)
    print(prostokat1.pole())
    print(prostokat1.obwod())


if __name__ == "__main__":
    main()


