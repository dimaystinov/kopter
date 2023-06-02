import math


class Drone:
    def __init__(self, x: float, y: float, angle: float):
        self.x: float = x
        self.y: float = y
        self.angle: float = angle

    def get_angle(self):
        return self.angle

    def set_angle(self, angle: float):
        self.angle = angle

    def rotate(self, angle: float):
        self.angle += angle
        if self.angle < 0:
            self.angle = math.pi * 2 - abs(self.angle)
        elif angle > 2 * math.pi:
            self.angle = self.angle - math.pi * 2

    def get_position(self):
        return self.x, self.y

    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x += x
        self.y += y


class Camera:
    def __init__(self, x_poi: float, y_poi: float, a: float):
        self.x_poi: float = x_poi
        self.y_poi: float = y_poi
        self.a: float = a

    def get_power_of_poi(self, drone: Drone):
        distance = math.sqrt((drone.x - self.x_poi) ** 2 + (drone.y - self.y_poi) ** 2)
        angle_to_point = math.atan((self.y_poi - drone.y) / (self.x_poi - drone.x))
        return self.a / (distance ** 2) * math.cos(angle_to_point - drone.angle)

    def get_position(self):
        return self.x_poi, self.y_poi
