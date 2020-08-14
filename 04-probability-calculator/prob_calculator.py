import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents: list = list()
        for color in kwargs:
            self.contents.extend([str(color).lower() for _ in range(kwargs[color])])

    def draw(self, balls_to_draw: int) -> list:
        random.shuffle(self.contents)  # randomizes our Hat
        balls_to_draw = (
            len(self.contents) if balls_to_draw > len(self.contents) else balls_to_draw
        )
        balls_drawn = []
        for _ in range(balls_to_draw):
            balls_drawn.append(self.contents.pop())
        return balls_drawn

    def __repr__(self):
        return str(self.contents)


def check_hats(balls_drawnm: list, expected_balls: dict) -> bool:
    """HELPER. Returns True if the expected_balls are contained in balls_drawn"""
    for color in expected_balls:
        if expected_balls.get(color) > balls_drawnm.count(color):
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    backup = copy.copy(hat.contents)
    positives = 0
    for _ in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        if check_hats(balls_drawn, expected_balls):
            positives += 1
        hat.contents = copy.copy(backup)
    return round(float(positives / num_experiments), 3)
