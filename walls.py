from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        """Creates the walls that bound the area where the ball is allowed to move."""

        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-243, -380)
        self.shape('square')
        self.color('white')
        self.shapesize(1, 2)
        self.seth(90)
        self.pensize(10)
        self.pendown()
        self.fd(670)
        self.right(90)
        self.fd(477)
        self.right(90)
        self.fd(670)
        self.penup()
