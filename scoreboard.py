from turtle import Turtle, Screen
from playsound import playsound


class Scoreboard(Turtle):
    def __init__(self):
        """Initializes the scoreboard, which is in charge of keeping track of lives,
        score and high score, and also displays that information to the player.
        The scoreboard class also is in charge of the instructions, tilt and game over screens."""

        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.current_score = 0
        with open("data.txt", mode="r") as file:
            high_score = file.readlines()
            self.name = str(high_score[0]).strip()
            self.high_score = int(high_score[1])
        self.instructions = True
        self.game_over = False
        self.tilt = False
        self.update()

    def update(self):
        """Displays the instructions screen before the game begins.
        Updates the scoreboard with the high score, the number of lives left and the current score.
        Displays the "tilt" and "game over" messages."""

        self.color('white')
        self.goto(-170, 350)
        self.write('HIGH SCORE', align='center', font=('Courier', 20, 'normal'))
        self.color('blue')
        self.goto(-170, 316)
        self.write(self.high_score, align='center', font=('Courier', 30, 'normal'))
        self.goto(-170, 300)
        self.write(self.name, align='center', font=('Courier', 15, 'normal'))
        self.color('white')
        self.goto(170, 350)
        self.write('YOUR SCORE', align='center', font=('Courier', 20, 'normal'))
        self.goto(170, 300)
        self.write(self.current_score, align='center', font=('Courier', 45, 'normal'))
        self.goto(0, 350)

        self.write('LIVES', align='center', font=('Courier', 20, 'normal'))
        self.shape('circle')
        self.color('purple')

        self.goto(-40, 325)
        self.shapesize(0.7, 0.7)
        if self.lives > 0:
            self.stamp()
            x = -40
            for step in range(self.lives - 1):
                x += 40
                self.goto(x, 325)
                self.stamp()

        if self.instructions:
            self.color('white')
            self.goto(0, -150)
            self.write(
                '   Press space bar to begin.\n\n'
                ' If the ball ever gets stuck\n'
                '  bouncing from wall to wall,\n'
                'press "t" to tilt the machine.',
                align='center',
                font=('Courier', 20, 'normal')
            )

        if self.game_over:
            self.color('white')
            self.goto(0, 0)
            self.write('GAME OVER', align='center', font=('Courier', 20, 'normal'))

        if self.tilt:
            self.color('white')
            self.goto(0, 0)
            self.write('TILT', align='center', font=('Courier', 20, 'normal'))

    def lose_life(self):
        """Processes the loss a life by subsctracting it from self.lives
        and plays a sound to give the player feedback.
        If the user ran out of lives, it plays the game over sound."""

        self.lives -= 1
        if self.lives > 0:
            playsound('game_sounds/lose_life.wav')
        else:
            playsound('game_sounds/game_over.wav')
        self.clear()
        self.update()

    def point(self, ammount):
        """Computes points gained by the player.
        Requires a positional argument "ammount" which determines the number of points gained."""

        self.current_score += ammount
        self.clear()
        self.update()

    def check_high_score(self):
        """Checks if the player's current score has surpassed the high score.
        If the player did, and it's the end of the game, check_high_score prompts the user
        to provide a 3 letter name for record."""

        if self.current_score > self.high_score:
            playsound('game_sounds/new_record.wav')
            screen = Screen()
            self.name = screen.textinput(
                title='New record!',
                prompt='You\'ve hit a new high score!\n     Type a 3-letters name.'
            ).upper()
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f'{self.name}\n{self.high_score}')
        self.clear()
        self.update()

    def remove_instructions(self):
        """Removes the instructions from the screen when the player starts the game."""

        self.instructions = False
        self.clear()
        self.update()
