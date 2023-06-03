import classes
import functions
import pygame_functions

if __name__ == "__main__":
    window = pygame_functions.Window()
    drone = classes.Drone(500, 500, 0)
    camera = classes.Camera(600, 600, 10000)
    points = classes.Points()
    count = 0
    while True:
        window.update(drone, camera, points)
        window.get_keyboard(drone)
        if count < 10:
            if functions.get_max(drone, camera, points):
                count += 1
                drone.fly(30, 30, 0.5)
                drone.check = True
                drone.max_angle = 0
                drone.max_power = 0
                drone.angle = 0.01

