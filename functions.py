import math
import classes
import pygame_functions
import setting


def get_max(drone: classes.Drone, camera: classes.Camera, points: classes.Points):
    if drone.check:
        drone.rotate(0.01)
        if drone.max_power < camera.get_power_of_poi_many_times(drone, setting.CHECKS_NUM):
            drone.max_power = camera.get_power_of_poi(drone)
            drone.max_angle = drone.angle
    else:
        drone.angle = drone.max_angle
        points.push(drone)
        return True
    if camera.get_power_of_poi(drone) < 0 and drone.max_angle:
        drone.angle = drone.max_angle
        points.push(drone)
        return True
    return False
