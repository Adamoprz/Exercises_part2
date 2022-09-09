import datetime


class Note:

    def __init__(self, author: str, text: str) -> None:
        self.author = author
        self.text = text
        self.date = datetime.datetime.now()

    def return_note(self) -> list:
        return [self.author, self.text, self.date]


class Notebook:
    def __init__(self) -> None:
        self.list_of_notes = []

    def add_note(self, author: str, text: str) -> None:
        new_note = Note(author, text)
        self.list_of_notes.append(new_note)

    def add_exist_note(self, n1) -> None:
        temp_note = n1
        self.list_of_notes.append(temp_note)

    def count_notes(self) -> None:
        print(len(self.list_of_notes))

    def show_notes(self) -> None:
        print("Masz takie notatki: ")
        for count, note in enumerate(self.list_of_notes):
            print(
                f'{count}.  {note.return_note()[0]}: "{note.return_note()[1]}" '
                f'o godzinie {note.return_note()[2].hour}:{note.return_note()[2].minute:02d}')


def main():
    nb = Notebook()
    nb.add_note("Bartek", "Dokonczyc instrukcje")
    nb.show_notes()
    # test time skip
    # time.sleep(60)
    n1 = Note("Andrii", "Sprawdzic instrukcje ")
    # test time skip
    # time.sleep(60)
    nb.add_exist_note(n1)
    nb.show_notes()


if __name__ == "__main__":
    main()
