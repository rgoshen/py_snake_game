from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    """Class for snake appearance and behavior."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        """Method for creating the starting head and 2 tail segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        """Method to add segments onto end of snake."""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)
        
    def reset(self):
        """Method to rest snake when collides with wall or own tail."""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def extend(self):
        """Method to extend snake."""
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        """Method to move snake forward and get tail to follow head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        """Method for moving the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        """Method for moving the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        """Method for moving the snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        """Method for moving the snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
