from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
step = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.pencolor("white")
        turtle.goto(position)
        self.segments.append(turtle)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(step)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        else:
            pass

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        else:
            pass

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        else:
            pass
