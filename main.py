import turtle as t
import random


screen = t.Screen()
screen.setup(width=500, height=400)
colors = ["Purple", "Blue", "Green", "Yellow", "Orange", "Red"]
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (Red, Green, Blue, "
                                               "Yellow, Purple, Orange)").capitalize()
turtles = []


def init_turtles(color, y_pos):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos)
    turtles.append(new_turtle)


def race():
    if bet:
        racing = True
    while racing:
        for racer in turtles:
            if racer.xcor() > 225:
                racing = False
                if racer.pencolor() == bet:
                    print(f"You won! The {racer.pencolor()} turtle was the fastest!")
                    return
                else:
                    print(f"You lose. The {racer.pencolor()} turtle won the race!")
                    return
            racer.forward(random.randint(1, 10))


if __name__ == '__main__':
    y = -90
    for turtle in colors:
        init_turtles(turtle, y)
        y += 35
    race()
    screen.exitonclick()
