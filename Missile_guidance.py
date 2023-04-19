import turtle
import math

time = 0
angle = 0


target_v_x = 4.37456
target_v_y = -3.34745
target_initial_location_x = -242
target_initial_location_y = 13.3476

projectile_initial_location_x = -34.375654365
projectile_initial_location_y = 3.3478563756
projectile_velocity = 0.1

target_location_y = target_initial_location_y
target_location_x = target_initial_location_x
projectile_location_y = projectile_initial_location_y
projectile_location_x = projectile_initial_location_x
projectile_v_x = projectile_velocity * 50 * math.cos(angle)
projectile_v_y = projectile_velocity * 50 * math.sin(angle)

target = turtle.Turtle()
projectile = turtle.Turtle()
target.color("blue")
projectile.color("red")
target.penup()
target.goto(target_initial_location_x,target_initial_location_y)
target.pendown()
projectile.penup()
projectile.goto(projectile_initial_location_x,projectile_initial_location_y)
projectile.pendown()

for x in range(0,100000):
    if math.isclose(target_location_x, projectile_location_x, abs_tol= 0.05):
        if math.isclose(target_location_y,projectile_location_y,abs_tol= 0.05):
            break
    else:
        time += 0.1
        target_location_x = time * target_v_x + target_initial_location_x
        target_location_y = time * target_v_y + target_initial_location_y
        angle = math.atan2(target_location_y - projectile_location_y, target_location_x - projectile_location_x)
        projectile_v_y = projectile_velocity * math.sin(angle)
        projectile_v_x = projectile_velocity * math.cos(angle)
        projectile_location_y = (projectile_v_y * time) + projectile_location_y
        projectile_location_x = (projectile_v_x * time) + projectile_location_x
        projectile.goto(projectile_location_x,projectile_location_y)
        target.goto(target_location_x,target_location_y)