from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    """Class for scoreboard for behavior and appearance."""
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write_score()
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.write_score()
        
    def reset(self):
        """Method to reset scoreboard and if current score is greater than
        stored high score then replace high score with current score.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
