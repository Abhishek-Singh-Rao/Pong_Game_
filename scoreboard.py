from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()
    def update_score(self):
        '''Display player's score.'''
        self.clear()
        self.goto(-120, 240)
        self.write(f"Left : {self.l_score}", align="center", font=("Arial", 20, "normal"))
        self.goto(120, 240)
        self.write(f"Right : {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def l_point(self):
        self.l_score += 1 # Increment left player score
        self.update_score() # Update score display
    def r_point(self):
        self.r_score += 1 # Increment right player score
        self.update_score() # Update score display
    def left_is_winner(self):
        self.goto(0, 0)
        self.write("Left is a Winner!", align="center", font=("Arial", 20, "normal")) # Display left player as winner

    def right_is_winner(self):
        self.goto(0, 0)
        self.write("Right is a Winner!", align="center", font=("Arial", 20, "normal"))  # Display right player as winner