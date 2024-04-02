# Import necessary modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turn off animation

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for key events
screen.listen()
# Right paddle moves up and down
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
# Left paddle moves up and down
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")


game_is_on = True

while game_is_on:

    # Controls ball speed
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    # Detect r_paddle misses
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

    # Check if a player has won
    if scoreboard.l_score == 5 and scoreboard.l_score > scoreboard.r_score:
        game_is_on = False # End game if left player wins
        scoreboard.left_is_winner() # Display winner message

    if scoreboard.r_score == 5 and scoreboard.r_score > scoreboard.l_score:
        game_is_on = False # End game if left player wins
        scoreboard.right_is_winner() # Display winner message


# Close the game window on click
screen.exitonclick()