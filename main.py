import classes
import functions
import pygame_functions

if __name__ == "__main__":
    window = pygame_functions.Window()
    drone = classes.Drone(500, 500, 0)
    camera = classes.Camera(600, 600, 10000)
    while True:
        window.get_keyboard(drone)
        window.update(drone, camera)
