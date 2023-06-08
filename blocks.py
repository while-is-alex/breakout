from turtle import Turtle
from playsound import playsound


class Blocks:
    def __init__(self):
        """Sets the level to the first one and initializes the blocks for that level.
        Keeps track of which blocks are currently on screen, each block's respective stamp-id
        and how many hits each block has taken."""

        self.level = 1

        self.green_blocks = []
        self.green_stamps = []

        self.yellow_blocks = []
        self.yellow_stamps = []
        self.yellow_hits = []

        self.orange_blocks = []
        self.orange_stamps = []
        self.orange_hits = []

        self.red_blocks = []
        self.red_stamps = []
        self.red_hits = []

        self.create_blocks()

    def create_blocks(self):
        """Initializes the blocks in the respective design for each level."""

        if self.level == 1:
            self.level_1_green()
            self.level_1_yellow()
            self.level_1_orange()
            self.level_1_red()

        elif self.level == 2:
            self.level_2_green()
            self.level_2_yellow()
            self.level_2_orange()
            self.level_2_red()

        elif self.level == 3:
            self.level_3_green()
            self.level_3_yellow()
            self.level_3_orange()
            self.level_3_red()

    def clear_level_check(self):
        """Checks if the level has been cleared by checking if there are still any blocks left.
        Increases the level, if there aren't any blocks left.
        Plays a sound as feedback for the player. Returns True if the level has been cleared."""

        if not self.green_blocks and not self.yellow_blocks and not self.orange_blocks and not self.red_blocks:
            playsound('game_sounds/level_up.wav')
            self.level += 1
            self.create_blocks()
            return True

    def destroy_green_block(self, block):
        """Destroys the current green block that has been hit."""

        if block in self.green_blocks:
            index = self.green_blocks.index(block)
            stamp = self.green_stamps[index]
            # Clears the block stamp from the screen
            block.clearstamp(stamp)
            # Removes the block and data connected to it from all green-blocks lists
            self.green_blocks.remove(block)
            self.green_stamps.remove(stamp)

    def destroy_yellow_block(self, block):
        """Adds one hit to the number of hits the yellow block has taken.
        If the number of hits is equal to 2, that block is destroyed."""

        if block in self.yellow_blocks:
            index = self.yellow_blocks.index(block)
            self.yellow_hits[index] += 1
            if self.yellow_hits[index] == 2:
                stamp = self.yellow_stamps[index]
                block.clearstamp(stamp)
                self.yellow_blocks.remove(block)
                self.yellow_stamps.remove(stamp)
                self.yellow_hits.remove(self.yellow_hits[index])

    def destroy_orange_block(self, block):
        """Adds one hit to the number of hits the orange block has taken.
        If the number of hits is equal to 3, that block is destroyed."""

        if block in self.orange_blocks:
            index = self.orange_blocks.index(block)
            self.orange_hits[index] += 1
            if self.orange_hits[index] == 3:
                stamp = self.orange_stamps[index]
                block.clearstamp(stamp)
                self.orange_blocks.remove(block)
                self.orange_stamps.remove(stamp)
                self.orange_hits.remove(self.orange_hits[index])

    def destroy_red_block(self, block):
        """Adds one hit to the number of hits the red block has taken.
        If the number of hits is equal to 4, that block is destroyed."""

        if block in self.red_blocks:
            index = self.red_blocks.index(block)
            self.red_hits[index] += 1
            if self.red_hits[index] == 4:
                stamp = self.red_stamps[index]
                block.clearstamp(stamp)
                self.red_blocks.remove(block)
                self.red_stamps.remove(stamp)
                self.red_hits.remove(self.red_hits[index])

    # Level 1
    def level_1_green(self):
        """Creates the green blocks in the design for the first level."""

        previous_turtle = 0
        for x in range(10):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            # Checks if it's the first block being created
            if not self.green_blocks:
                turtle.goto(-212, 110)
            # If it isn't, it uses the position of the previous block as reference
            else:
                x = self.green_blocks[previous_turtle].xcor() + 46
                y = 110
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('green')
            turtle.shapesize(1, 2)
            # Creates a stamp, which is the visual representation of a block,
            # and saves its id into a variable, so that stamp can be found again later
            stamp_id = turtle.stamp()
            self.green_blocks.append(turtle)
            self.green_stamps.append(stamp_id)

    def level_1_yellow(self):
        """Creates the yellow blocks in the design for the first level."""

        previous_turtle = 0
        for x in range(10):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.yellow_blocks:
                turtle.goto(-212, 135)
            else:
                x = self.yellow_blocks[previous_turtle].xcor() + 46
                y = 135
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('yellow')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.yellow_blocks.append(turtle)
            self.yellow_stamps.append(stamp_id)
            self.yellow_hits.append(0)

    def level_1_orange(self):
        """Creates the orange blocks in the design for the first level."""

        previous_turtle = 0
        for x in range(10):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.orange_blocks:
                turtle.goto(-212, 160)
            else:
                x = self.orange_blocks[previous_turtle].xcor() + 46
                y = 160
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('orange')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.orange_blocks.append(turtle)
            self.orange_stamps.append(stamp_id)
            self.orange_hits.append(0)

    def level_1_red(self):
        """Creates the red blocks in the design for the first level."""

        previous_turtle = 0
        for x in range(10):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.red_blocks:
                turtle.goto(-212, 185)
            else:
                x = self.red_blocks[previous_turtle].xcor() + 46
                y = 185
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('red')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.red_blocks.append(turtle)
            self.red_stamps.append(stamp_id)
            self.red_hits.append(0)

    # Level 2
    def level_2_green(self):
        """Creates the green blocks in the design for the second level."""

        # Keeps track of what's the line that columns are being created for
        line = 1
        # Loops through the code that generates 4 columns of blocks
        for z in range(2):
            previous_turtle = 0

            if line == 1:
                y = 210
            elif line == 2:
                y = 35
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if not self.green_blocks or len(self.green_blocks) == 12:
                    turtle.goto(-190, y)
                else:
                    x = self.green_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('green')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.green_blocks.append(turtle)
                self.green_stamps.append(stamp_id)

            y = y - 25
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 3:
                    turtle.goto(-145, y)
                    previous_turtle += 1
                else:
                    x = self.green_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('green')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.green_blocks.append(turtle)
                self.green_stamps.append(stamp_id)

            y = y - 75
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 7:
                    turtle.goto(-145, y)
                    previous_turtle += 1
                else:
                    x = self.green_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('green')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.green_blocks.append(turtle)
                self.green_stamps.append(stamp_id)

            line += 1

    def level_2_yellow(self):
        """Creates the yellow blocks in the design for the second level."""

        line = 1
        for z in range(2):
            previous_turtle = 0

            if line == 1:
                y = 160
            elif line == 2:
                y = -15
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if not self.yellow_blocks or len(self.yellow_blocks) == 8:
                    turtle.goto(-190, y)
                else:
                    x = self.yellow_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('yellow')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.yellow_blocks.append(turtle)
                self.yellow_stamps.append(stamp_id)
                self.yellow_hits.append(0)

            y = y - 25
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 3:
                    turtle.goto(-145, y)
                    previous_turtle += 1
                else:
                    x = self.yellow_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('yellow')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.yellow_blocks.append(turtle)
                self.yellow_stamps.append(stamp_id)
                self.yellow_hits.append(0)

            line += 1

    def level_2_orange(self):
        """Creates the orange blocks in the design for the second level."""

        line = 1
        for z in range(2):
            previous_turtle = 0

            if line == 1:
                y = 210
            elif line == 2:
                y = 35
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if not self.orange_blocks or len(self.orange_blocks) == 8:
                    turtle.goto(-145, y)
                else:
                    x = self.orange_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('orange')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.orange_blocks.append(turtle)
                self.orange_stamps.append(stamp_id)
                self.orange_hits.append(0)

            y = y - 75
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 3:
                    turtle.goto(-190, y)
                    previous_turtle += 1
                else:
                    x = self.orange_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('orange')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.orange_blocks.append(turtle)
                self.orange_stamps.append(stamp_id)
                self.orange_hits.append(0)

            line += 1

    def level_2_red(self):
        """Creates the red blocks in the design for the second level."""

        line = 1
        for z in range(2):
            previous_turtle = 0

            if line == 1:
                y = 185
            if line == 2:
                y = 10
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if not self.red_blocks or len(self.red_blocks) == 12:
                    turtle.goto(-190, y)
                else:
                    x = self.red_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('red')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.red_blocks.append(turtle)
                self.red_stamps.append(stamp_id)
                self.red_hits.append(0)

            y = y - 25
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 3:
                    turtle.goto(-145, y)
                    previous_turtle += 1
                else:
                    x = self.red_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('red')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.red_blocks.append(turtle)
                self.red_stamps.append(stamp_id)
                self.red_hits.append(0)

            y = y - 50
            for x in range(4):
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                if previous_turtle == 7:
                    turtle.goto(-190, y)
                    previous_turtle += 1
                else:
                    x = self.red_blocks[previous_turtle].xcor() + 110
                    turtle.goto(x, y)
                    previous_turtle += 1
                turtle.shape('square')
                turtle.color('red')
                turtle.shapesize(1, 2)
                stamp_id = turtle.stamp()
                self.red_blocks.append(turtle)
                self.red_stamps.append(stamp_id)
                self.red_hits.append(0)

            line += 1

    # Level 3
    def level_3_green(self):
        """Creates the green blocks in the design for the third level."""

        previous_turtle = 0
        for x in range(4):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.green_blocks:
                y = 185
                turtle.goto(-85, y)
            else:
                x = self.green_blocks[previous_turtle].xcor() + 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('green')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.green_blocks.append(turtle)
            self.green_stamps.append(stamp_id)

        for x in range(6):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 4:
                y = 185
                turtle.goto(75, y)
                previous_turtle += 1
            else:
                x = self.green_blocks[previous_turtle].xcor() - 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('green')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.green_blocks.append(turtle)
            self.green_stamps.append(stamp_id)

    def level_3_yellow(self):
        """Creates the yellow blocks in the design for the third level."""

        previous_turtle = 0
        for x in range(8):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.yellow_blocks:
                y = 185
                turtle.goto(-125, y)
            else:
                x = self.yellow_blocks[previous_turtle].xcor() + 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('yellow')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.yellow_blocks.append(turtle)
            self.yellow_stamps.append(stamp_id)
            self.yellow_hits.append(0)

        for x in range(7):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 8:
                y = 185
                turtle.goto(115, y)
                previous_turtle += 1
            else:
                x = self.yellow_blocks[previous_turtle].xcor() - 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('yellow')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.yellow_blocks.append(turtle)
            self.yellow_stamps.append(stamp_id)
            self.yellow_hits.append(0)

    def level_3_orange(self):
        """Creates the orange blocks in the design for the third level."""

        previous_turtle = 0
        for x in range(9):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.orange_blocks:
                y = 185
                turtle.goto(-165, y)
            else:
                x = self.orange_blocks[previous_turtle].xcor() + 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('orange')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.orange_blocks.append(turtle)
            self.orange_stamps.append(stamp_id)
            self.orange_hits.append(0)

        for x in range(8):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 8:
                y = 185
                turtle.goto(155, y)
                previous_turtle += 1
            else:
                x = self.orange_blocks[previous_turtle].xcor() - 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('orange')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.orange_blocks.append(turtle)
            self.orange_stamps.append(stamp_id)
            self.orange_hits.append(0)

        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        y = 185
        turtle.goto(-5, y)
        previous_turtle += 1
        turtle.shape('square')
        turtle.color('orange')
        turtle.shapesize(1, 2)
        stamp_id = turtle.stamp()
        self.orange_blocks.append(turtle)
        self.orange_stamps.append(stamp_id)
        self.orange_hits.append(0)

    def level_3_red(self):
        """Creates the red blocks in the design for the third level."""

        previous_turtle = 0
        for x in range(11):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if not self.red_blocks:
                y = 185
                turtle.goto(-205, y)
            else:
                x = self.red_blocks[previous_turtle].xcor() + 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('red')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.red_blocks.append(turtle)
            self.red_stamps.append(stamp_id)
            self.red_hits.append(0)

        for x in range(10):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 10:
                y = 185
                turtle.goto(195, y)
                previous_turtle += 1
            else:
                x = self.red_blocks[previous_turtle].xcor() - 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('red')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.red_blocks.append(turtle)
            self.red_stamps.append(stamp_id)
            self.red_hits.append(0)

        for x in range(3):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 20:
                y = 185
                turtle.goto(-45, y)
                previous_turtle += 1
            else:
                x = self.red_blocks[previous_turtle].xcor() + 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('red')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.red_blocks.append(turtle)
            self.red_stamps.append(stamp_id)
            self.red_hits.append(0)

        for x in range(2):
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            if previous_turtle == 23:
                y = 185
                turtle.goto(35, y)
                previous_turtle += 1
            else:
                x = self.red_blocks[previous_turtle].xcor() - 20
                y = y - 20
                turtle.goto(x, y)
                previous_turtle += 1
            turtle.shape('square')
            turtle.color('red')
            turtle.shapesize(1, 2)
            stamp_id = turtle.stamp()
            self.red_blocks.append(turtle)
            self.red_stamps.append(stamp_id)
            self.red_hits.append(0)

