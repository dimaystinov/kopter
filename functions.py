import math
import classes
import pygame_functions

def get_max(drone: classes.Drone, camera: classes.Camera):
    if drone.check:
        drone.rotate(0.01)
        power = camera.get_power_of_poi(drone)
        if power > drone.max_power:
            drone.max_angle = drone.angle
            drone.max_power = power
    else:
        drone.set_angle(drone.max_angle)
    if drone.get_angle() == 0:
        drone.check = False
