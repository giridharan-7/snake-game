from turtle import Turtle
starting_positions = [(0,0),(-20,0),(-40,0)]
move_dis=20
up=90
down=270
left=180
right=0
class Snake:
    # Using the self parameter allows you to access and
    # modify the attributes and methods of the instance inside the class methods.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in starting_positions:
            self.add_segment(pos)

    def add_segment(self,position):
        tur1 = Turtle("square")
        tur1.color("white")
        tur1.penup()
        tur1.goto(position)
        self.segments.append(tur1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_dis)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
