from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Ball bounces when collide with wall.
    def bounce_y(self):
        self.y_move *= -1

    # Increase speed of ball when collide with paddle.
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    # Ball bounces when collide with paddle
    def paddle_bounce(self):
        self.x_move *= -1
        self.y_move *= -1

    # Reset ball's position to origin when missed by any player
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
