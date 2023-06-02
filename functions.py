import classes
import pygame_functions


def init():
    drone = classes.Drone(5, 5, 0)
    camera = classes.Camera(10, 10, 10000)
    print(camera.get_power_of_poi(drone))