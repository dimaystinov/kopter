import math
import random

class Drone:
    def __init__(self, x: float, y: float, angle: float):
        self.x: float = x
        self.y: float = y
        self.angle: float = angle
        self.check: bool = True
        self.max_angle = 0
        self.max_power = 0

    def get_angle(self):
        return self.angle

    def set_angle(self, angle: float):
        self.angle = angle

    def rotate(self, angle: float):
        self.angle += angle
        if self.angle < 0:
            self.angle = math.pi * 2 - abs(self.angle)
            self.check = False
        elif self.angle > 2 * math.pi:
            self.angle = self.angle - math.pi * 2
            self.check = False
        self.angle = round(self.angle, 2)

    def get_position(self):
        return self.x, self.y

    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x += x
        self.y += y

    def fly(self, x: float, y: float, z: float):
        self.y += math.sin(self.angle - z * math.pi) * y
        self.x += math.cos(self.angle - z * math.pi) * x



class Camera:
    def __init__(self, x_poi: float, y_poi: float, a: float):
        self.x_poi: float = x_poi
        self.y_poi: float = y_poi
        self.a: float = a

    def get_power_of_poi(self, drone: Drone):
        distance = math.sqrt((drone.x - self.x_poi) ** 2 + (drone.y - self.y_poi) ** 2)
        angle_to_point = math.atan2((self.y_poi - drone.y),(self.x_poi - drone.x))
        return self.a / (distance ** 2) * math.cos(angle_to_point - drone.angle) #* float(random.randint(70, 120)
                                                                                  #           / 100)

    def get_power_of_poi_pos(self, x: float, y: float, angle: float):
        distance = math.sqrt((x - self.x_poi) ** 2 + (y - self.y_poi) ** 2)
        angle_to_point = math.atan2((self.y_poi - y), (self.x_poi - x))
        return self.a / (distance ** 2) * math.cos(angle_to_point - angle) * float(random.randint(70, 120) / 100)

    def get_power_of_poi_many_times(self, drone: Drone, times: int = 0):
        all = 0
        for i in range(times):
            all += self.get_power_of_poi(drone)
        return all/times


    def get_position(self):
        return self.x_poi, self.y_poi


class Points:
    def __init__(self):
        self.back = []

    def push(self, drone: Drone):
        self.back.append((drone.get_position(), drone.get_angle()))

    def get_all_points(self):
        return self.back
