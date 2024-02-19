class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height: height

    @property
    def area(self) -> int:
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Width: {self._width}, height: {self._height}'

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int) -> None:
        self._height = value


    @width.setter
    def width(self, value: int) -> None:
        self._width = value


class Square(Rectangle):
    
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value: int) -> None:
        self._width = self._height = value

    
    @Rectangle.height.setter
    def height(self, value: int) -> None:
        self._height = self._width = value


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)