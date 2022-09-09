from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you guess", prompt="Which turtle will win the race? Enter a color: ")
turtles = []
turtle_color = ["red", "orange","yellow", "blue", "green", "purple"]


y_position = -160
for _ in range(6):
    turtle = Turtle(shape="turtle")
    turtles.append(turtle)
    turtle.color(turtle_color[_])
    turtle.penup()
    turtle.speed("fastest")
    turtle.goto(-230, y_position)
    y_position += 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() == 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won!, {winning_color} turtle is the winner!")
            else:
                print(f"You've lose!, {winning_color} turtle is the winner!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





screen.exitonclick()