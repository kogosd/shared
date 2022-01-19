from math import *
from this import d
import turtle

TURTLE = False
sqrt3= sqrt(3.)
if TURTLE: 
    board = turtle.Turtle()
    board.speed(0)    
scale=100
EPSILON = 1e-8


def clear():
    if TURTLE==False: return    
    board.reset()

def draw_title(s):
    if TURTLE==False: return
    board.penup()
    board.goto(0, 5*scale)
    board.pendown()
    board.write(s)

def draw_triangle(x,y, slope=0):
    if TURTLE==False: return
    board.penup()
    board.goto(x*scale, y*scale)
    board.pendown()
    board.right(1*scale)
    board.setheading(60+slope)
    board.forward(1*scale)
    board.setheading(-60+slope)
    board.forward(1*scale)
    board.setheading(180+slope)
    board.forward(1*scale)

def draw_triangle_from_current(x,y, slope=0):
    if TURTLE==False: return    
    board.pendown()
    board.right(1*scale)
    board.setheading(60+slope)
    board.forward(1*scale)
    board.setheading(-60+slope)
    board.forward(1*scale)
    board.setheading(180+slope)
    board.forward(1*scale)


def draw_rectangle(x,y, x1,y1, x2,y2, x3,y3):
    if TURTLE==False: return    
    board.pensize(2)
    board.penup()
    board.goto(x*scale, y*scale)
    board.pendown()
    board.goto(x1*scale,y1*scale)
    board.goto(x2*scale,y2*scale)
    board.goto(x3*scale,y3*scale)
    board.goto(x*scale,y*scale)
    board.pensize(1)

def draw_line(x1,y1, x2,y2):
    if TURTLE==False: return    
    board.penup()
    board.goto(x1*scale, y1*scale)
    board.pendown()
    board.goto(x2*scale,y2*scale)

def draw_triangles_along_line(x1, y1, x2, y2, N):
    if TURTLE==False: return    
    draw_line(x1,y1, x2, y2)
    slope = degrees(atan((y2-y1)/(x2-x1)))
    print(f"slope={slope} y2-y1={y2-y1} x2-x1={x2-x1}")
    draw_triangle(x1, y1, slope)
    board.setheading(slope)
    board.forward(1*scale)
    while N>1: 
        draw_triangle_from_current(turtle.pos()[0], turtle.pos()[1], slope)
        board.setheading(slope)
        board.forward(1*scale)
        N-=1


def wait():
    if TURTLE==False: return    
    print("Waiting for input")
    if TURTLE: rc = input()

if __name__ == '__main__':
    draw_rectangle(0,0, 0,-1, -sqrt(3.), -1, -sqrt(3.), 0)
    draw_line(-sqrt(3.),0,0,-1)
    draw_triangles_along_line(-sqrt(3.),0, 0, -1., 3)      
    draw_triangles_along_line(-sqrt(3.)-sqrt(3),0, 0-sqrt(3), -1., 3)          
    wait()  