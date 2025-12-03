import turtle
import time
import random


WIDTH = 500
HEIGHT = 500
COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "purple",
    "pink",
    "cyan",
    "brown",
    "gray",
]


def init_turtle(WIDTH, HEIGHT):
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.setup(WIDTH, HEIGHT)
    return screen


def get_number_of_racers():
    while True:
        tutel_racers = input("Введите количество черепах для гонки (от 2 до 10): ")
        if not tutel_racers.isdigit():
            print("Вы ввели не число")
            continue
        tutel_racers = int(tutel_racers)
        if tutel_racers < 2 or tutel_racers > 10:
            size = "маленькое" if tutel_racers < 2 else "большое"
            print(f"Вы ввели слишком {size} число")
            continue
        else:
            print(f"В гонке {tutel_racers} участников")
            break
    return tutel_racers


def create_turtles(colors, WIDTH, HEIGHT):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.left(90)
        t.penup()

        x = -WIDTH // 2 + (i + 1) * spacing
        y = -HEIGHT // 2 + 20
        t.setpos(x, y)
        t.pendown()
        turtles.append(t)
    return turtles


def race(colors, HEIGHT, WIDTH):
    turtles = create_turtles(colors, WIDTH, HEIGHT)
    while True:
        for t in turtles:
            distance = random.randint(1, 20)
            t.forward(distance)
            x, y = t.pos()
            if y >= HEIGHT // 2 - 10:
                winner = t.color()[0]
                return winner


def main():
    colors_ru = {
        "red": "красного",
        "green": "зелёного",
        "blue": "синего",
        "orange": "оранжевого",
        "yellow": "жёлтого",
        "purple": "фиолетового",
        "pink": "розового",
        "cyan": "голубого",
        "brown": "коричневого",
        "gray": "серого",
    }

    tutel_racers = get_number_of_racers()
    init_turtle(WIDTH, HEIGHT)
    random.shuffle(COLORS)
    colors = COLORS[:tutel_racers]
    winner_color = race(colors, HEIGHT, WIDTH)
    winner_rucolor = colors_ru[winner_color]
    print(f"Победила черепаха {winner_rucolor} цвета!")


if __name__ == "__main__":
    main()
