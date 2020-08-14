from typing import TypeVar, Sized

RectangleType = TypeVar("Rectangle")
SquareType = TypeVar("Square")


class Rectangle:
    def __init__(self, width: int, height: int):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_amount_inside(self, other: RectangleType) -> int:
        area_other = other.get_area()
        area_own = self.get_area()
        return round(area_own // area_other, 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        rect = ""
        for _ in range(self.height):
            rect += f"{'*' * self.width}\n"
        return rect

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side: int):
        self.side = side
        super().set_height(side)
        super().set_width(side)

    def set_height(self, height: int):
        self.set_side(height)

    def set_width(self, width: int):
        self.set_side(width)

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.side})"

