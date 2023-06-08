from turtle import Turtle


class Paddle:
    """Initializes the paddle, sets it in position and starts listening for key presses."""

    def __init__(self, position):
        self.paddle = []
        self.x, self.y = position
        self.position = (self.x, self.y)
        self.move_speed = 25
        self.create_paddle()

    def create_paddle(self):
        """Creates the paddle by creating 3 separate turtles (left, middle and right),
        which together make up the paddle."""

        left_side = Turtle()
        left_side.goto(self.position)
        left_side.shape("square")
        left_side.color("white")
        left_side.shapesize(stretch_wid=1, stretch_len=2)
        left_side.penup()
        self.paddle.append(left_side)

        middle = Turtle()
        middle.goto(self.x + 30, self.y)
        middle.shape("square")
        middle.color("white")
        middle.shapesize(stretch_wid=1, stretch_len=1)
        middle.penup()
        self.paddle.append(middle)

        right_side = Turtle()
        right_side.goto(self.x + 60, self.y)
        right_side.shape("square")
        right_side.color("white")
        right_side.shapesize(stretch_wid=1, stretch_len=2)
        right_side.penup()
        self.paddle.append(right_side)

    def left(self):
        """Loops through each part of the paddle making sure it moves in synch
        towards the left."""

        for paddle_part in self.paddle:
            new_x = paddle_part.xcor() - self.move_speed
            paddle_part.goto(new_x, paddle_part.ycor())

    def right(self):
        """Loops through each part of the paddle making sure it moves in synch
        towards the right."""

        for paddle_part in self.paddle:
            new_x = paddle_part.xcor() + self.move_speed
            paddle_part.goto(new_x, paddle_part.ycor())
