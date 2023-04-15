from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.style = ('Courier',15,'bold')
        self.score = -1
        with open("data.txt", mode="r") as rd:
            self.h_s = int(rd.read())
        self.update()

    def update(self):
        self.score+=1
        self.penup()
        self.hideturtle()
        self.goto(0,278)
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.h_s}", font=self.style, align="center")

    def reset(self):
        if self.score > self.h_s:
            self.h_s = self.score
        self.score = -1
        with open("data.txt", mode="w") as file:
            file.write(str(self.h_s))
        self.update()