from turtle import Turtle, Screen
import random


class Ball(Turtle):
    def __init__(self):
        """Initializes the ball, settings its initial movement speed and its starting position."""

        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.goto(0, -200)
        self.move_speed = 4
        self.running = False
        self.bounceable = True
        self.tilt = 0

    def set(self):
        """Sets the ball at an angle pointing upwards."""

        random_angle = random.randrange(0, 180)
        self.setheading(random_angle)

    def move(self):
        """Makes the ball move forward."""

        self.forward(self.move_speed)

    def bounce_y(self, part=None):
        """Bounces the ball towards the opposite direction vertically.
        Checks if the ball is bouncing off the paddle or off the ceiling."""

        # Checks if the ball is colliding with the left,
        # middle or right part of the paddle
        if part:
            if part == 1:
                angle = random.randrange(90, 160)
                self.setheading(angle)
            elif part == 2:
                angle = random.randrange(80, 100)
                self.setheading(angle)
            elif part == 3:
                angle = random.randrange(20, 90)
                self.setheading(angle)
        # Bouncing off top wall
        else:
            self.setheading(360 - self.heading())

    def bounce_x(self):
        """Bounces the ball towards the opposite direction horizontally."""

        self.setheading(180 - self.heading())

    def block_bounce(self, screen):
        """Bounces the ball off blocks.
        Checks the attribute "bounceable" to check if the ball is ready to bounce again.
        Requires a position argument "screen" of type turtle.Screen."""

        if self.bounceable:
            self.setheading(self.heading() * -1)
            self.bounceable = False
            screen.ontimer(self.make_bounceable, t=500)

    def ball_reset(self):
        """Resets the ball to the starting position and at an upwards angle."""

        self.goto(0, -200)
        self.set()

    def make_bounceable(self):
        """Sets the attribute "self.bounceable" to True."""

        self.bounceable = True

    def tilt_table(self):
        """Sets the heading of the ball to a 45-degree angle and adds 1 to the attribute
        which keeps track of the number of times the player "tilted the machine"."""

        self.setheading(45)
        self.tilt += 1

    def start_moving(self):
        """Allows the ball to start moving."""

        self.running = True
