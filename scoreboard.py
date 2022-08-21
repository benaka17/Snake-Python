from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.writeScore()


    def writeScore(self):
        self.clear()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
        #self.score += 1

    def gameOver(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER. \n Score: {self.score}", align=ALIGNMENT, font=FONT)
