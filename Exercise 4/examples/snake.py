import random
from collections import namedtuple

from machine import I2C, Pin
from sh1106 import SH1106_I2C
from utime import sleep

game_width = 128
game_height = 64
start_x = 0
start_y = 30
snake_length = 15


left_button = Pin(18, Pin.IN, Pin.PULL_UP)
up_button = Pin(19, Pin.IN, Pin.PULL_UP)
down_button = Pin(20, Pin.IN, Pin.PULL_UP)
right_button = Pin(21, Pin.IN, Pin.PULL_UP)

Position = namedtuple("Position", ["x", "y"])


class Snake:
    def __init__(self, screen: SH1106_I2C) -> None:
        self.screen: SH1106_I2C = screen
        self.score: int = 0
        self.length = snake_length
        self.pos: list[Position] = []
        self.direction = "right"
        self.fruit: Position = Position(
            random.randint(snake_length + 20, game_width - 20), random.randint(10, game_height - 10)
        )

    def initialize_snake(self) -> None:
        for l in range(self.length):
            self.pos.insert(0, Position(start_x + l, start_y))
        self.draw()
        self.screen.show()

    def make_fruit(self) -> None:
        on_snake = True
        while on_snake:
            fruit_location = Position(
                random.randint(10, game_width - 10), random.randint(5, game_height - 5)
            )
            on_snake = fruit_location in self.pos
        self.screen.pixel(self.fruit.x, self.fruit.y, 0)  # Clear old fruit location
        self.fruit = fruit_location

    def move(self) -> Position | None:
        "Return the old end position of the snake if needed"
        head = self.pos[0]
        if self.direction == "up":
            new_head = Position(head.x, (head.y - 1) % game_height)
        if self.direction == "down":
            new_head = Position(head.x, (head.y + 1) % game_height)
        if self.direction == "left":
            new_head = Position((head.x - 1) % game_width, head.y)
        if self.direction == "right":
            new_head = Position((head.x + 1) % game_width, head.y)
        if new_head in self.pos:
            raise ValueError()
        self.pos.insert(0, new_head)
        if new_head == self.fruit:
            self.make_fruit()
            self.length = int(self.length * 1.2)
            self.score += 1
            return None
        return self.pos.pop(-1)

    def draw(self) -> None:
        for pos in self.pos:
            self.screen.pixel(pos.x, pos.y, 1)
        self.screen.pixel(self.fruit.x, self.fruit.y, 1)

    def tick(self) -> None:
        old_end = self.move()
        if old_end:
            self.screen.pixel(old_end.x, old_end.y, 0)
        self.draw()
        self.screen.show()


i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
oled = SH1106_I2C(128, 64, i2c, None, addr=0x3C)
oled.sleep(False)
oled.show()

snake = Snake(screen=oled)
snake.initialize_snake()
while True:
    try:
        if left_button.value() == 0 and snake.direction != "right":
            snake.direction = "left"
        if right_button.value() == 0 and snake.direction != "left":
            snake.direction = "right"
        if up_button.value() == 0 and snake.direction != "down":
            snake.direction = "up"
        if down_button.value() == 0 and snake.direction != "up":
            snake.direction = "down"
        snake.tick()
        sleep(0.033)
    except KeyboardInterrupt:
        break
    except ValueError:
        oled.fill(0)
        oled.text(f"Your score: {snake.score}", 15, 30)
        oled.flip()
        oled.show()
        break
