import turtle
import os
import math
import time
import sys
os.system('clear')

time_for_hit = 0
duration = time_for_hit

target_initial_x = 0
target_initial_y = 0
def target_velocity_x():
    target_v_x = 0
    return target_v_x
def target_velocity_y():
    target_v_y = 0
    return target_v_y

missile_initial_x = 0
missile_initial_y = 0

contact_x = time_for_hit * target_velocity_x() + target_initial_x
contact_y = time_for_hit * target_velocity_y() + target_initial_y

missile_v_x = (contact_x - missile_initial_x) / time_for_hit
missile_v_y = (contact_y - missile_initial_y) / time_for_hit

target = turtle.Turtle()
target.color('blue')
missile = turtle.Turtle()
missile.color('red')
missile.penup()
target.penup()
target.shape('circle')
missile.shape('circle')
missile.shapesize(0.5,0.5)
target.shapesize(0.5,0.5)
turtle.bgcolor('black')
screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

duration = 0

while True:
    missile_x = missile_initial_x + (missile_v_x * duration)
    missile_y = missile_initial_y + (missile_v_y * duration)
    target_x = target_initial_x + (target_velocity_x() * duration)
    target_y = target_initial_y + (target_velocity_y() * duration)
    target_velocity_x()
    target_velocity_y()
    missile.goto(missile_x,missile_y)
    target.goto(target_x,target_y)
    duration += 0.1
    missile.pendown()
    target.pendown()
    if math.isclose(target_x, missile_x, rel_tol= 0.001):
        if math.isclose(target_y, missile_y, rel_tol= 0.001):
            time.sleep(3)
            sys.exit()
