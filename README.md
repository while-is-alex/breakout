# Breakout
Breakout game built with Python and Turtle graphics. The objective of the game is destroying all the colored blocks from every level by hitting them with the ball.

## Getting started
1. Clone the repository:
```
git clone https://github.com/while-is-alex/breakout.git
```

2. Change the directory to the project folder.

3. Create a virtual environment:
```
py -m venv venv
venv/Scripts/activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Finally, to get the game started, run the `main.py` file. The game will launch and display the home screen.

![instructions.png](https://i.ibb.co/Yt32kNC/instructions.png)

## Features

### Gameplay
The game starts after the user went through the instructions screen and only after the user presses space bar is that the ball starts moving. The user starts the game with 3 lives, displayed at the top of the screen. Also displayed at the top of the screen are the current game's score and also the all-time high score. The user has to not let the ball fall past the paddle at the bottom of the screen or else they'll lose a life. The objective is to deflect the ball upwards towards the colored blocks in order to break them. Each block-color takes a different number of hits to be broken (green: 1, yellow: 2, orange: 3 and red: 4). The game pleasantly provides unique audio feedback to each ball-hits (to paddle, walls and blocks).

![gameplay.png](https://i.ibb.co/4KrTr67/gameplay.png)

### Game over
If the user loses all of their lives, the game ends.

![game-over.png](https://i.ibb.co/vLv6pJF/game-over.png)

### Tilt

The player has the option of "tilting the machine" (pressing "t" on the keyboard), just like in old arcades, in order to affect the ball's trajectory to remove it from a loop or to cheat themselves out of a death. However, as that move is illegal, if the player tilts the machine too many times, the game will end and the player will be presented with a tilt error.

![]()

## Requirements

This app requires the following:

+ Python 3
+ Turtle graphics
+ Playsound
