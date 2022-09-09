
class Shape:
    def __init__(self, name: str, length: float) -> None
        self.name = name

    def calc_area(self) -> None:
        return 0


class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length
        super().__init__('square', self.length)

    def calc_area(self):
        return self.length ** 2


sq = Square(123)
print(sq.calc_area())