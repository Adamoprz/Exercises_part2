class Menu:

    def __init__(self) -> None:
        pass

    def show(self) -> None

        print('1. Dodaj notatkę')
        print('2. Dodaj wizytówkę (Card)')
        print('3. Wyświetl wszystkie notatki')
        print('4. Wyświetl wszystkie wizytówki')
        print('5. Wyjdź')

    def get_choice(self) -> None:
        choice = int(input('Wybierz funkcje \n'))

class Manager(Menu):

    def __init__(self) -> None:
        pass

    def start(self) -> None:
        self.if_start = True
        self.show_menu()

    def show_menu(self) -> None:
        m = Menu()
        m.show()

    def execute(self) -> None:
        choice = int(input('Wybierz funkcje \n'))


    def show_notes(self):
        pass

    def show_cards(self):
        pass




class NotesSubManager:
    def __init__(self):
        '''lista na obiekty reprezentujace
        dodane Notatki/Wizytowki'''
        notes = []

    def add(self):
        pass

    def show(self):
        pass

class CardSubManager:
    def __init__(self):
        '''lista na obiekty reprezentujace
        dodane Notatki/Wizytowki'''
        cards = []

    def add(self):
        pass

    def show(self):
        pass

def main():
    m2 = Manager()
    m2.start()


if __name__ == "__main__":
    main()
