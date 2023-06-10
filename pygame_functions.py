import math

import pygame
import setting
import classes


class Window:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
        pygame.display.set_caption("CoPtEr Z")
        self.clock = pygame.time.Clock()

    @staticmethod
    def get_keyboard(drone: classes.Drone):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        if keys[pygame.K_w]:
            drone.fly(1, 1, 0)
        if keys[pygame.K_s]:
            drone.fly(-1, -1, 0)
        if keys[pygame.K_a]:
            drone.fly(1, 1, 0.5)
        if keys[pygame.K_d]:
            drone.fly(1, 1, -0.5)
        if keys[pygame.K_e]:
            drone.rotate(-0.01)
        if keys[pygame.K_q]:
            drone.rotate(0.01)

    def update(self, drone: classes.Drone, camera: classes.Camera, points: classes.Points):
        self.screen.fill(setting.FIELD_COLOR)
        x2, y2 = drone.get_position()
        x2 = x2 + 10000 * math.cos(drone.max_angle)
        y2 = y2 + 10000 * math.sin(drone.max_angle)
        pygame.draw.line(self.screen, setting.DRONE_COLOR, drone.get_position(), (x2, y2), setting.THICKNESS_DRONE_LINE)
        x2, y2 = drone.get_position()
        x2 = x2 + 10000 * math.cos(drone.get_angle())
        y2 = y2 + 10000 * math.sin(drone.get_angle())
        pygame.draw.line(self.screen, setting.POI_COLOR, drone.get_position(), (x2, y2), setting.THICKNESS_DRONE_LINE)

        pygame.draw.circle(self.screen, setting.DRONE_COLOR, drone.get_position(), setting.RADIUS_DRONE)
        pygame.draw.circle(self.screen, setting.POI_COLOR, camera.get_position(), setting.RADIUS_POI)
        for i in points.get_all_points():
            pygame.draw.circle(self.screen, setting.LAST_COLOR, i[0], setting.RADIUS_DRONE)
            x2, y2 = i[0]
            x2 = x2 + 10000 * math.cos(i[1])
            y2 = y2 + 10000 * math.sin(i[1])
            pygame.draw.line(self.screen, setting.LAST_COLOR, i[0], (x2, y2),
                             setting.THICKNESS_DRONE_LINE)
        point_x = 0
        point_y = 0
        count_points = 0
        if len(points.get_all_points()) > 1:
            for i in points.get_all_points():
                for j in points.get_all_points():
                        if i != j:
                                k1 = math.tan(i[1])
                                b1 = i[0][1] - k1 * i[0][0]
                                k2 = math.tan(j[1])
                                b2 = j[0][1] - k2 * j[0][0]
                                if k1 == k2:
                                    continue
                                point_x += (b2 - b1) / (k1 - k2)
                                point_y += k1 * (b2 - b1) / (k1 - k2) + b1
                                count_points += 1
            point_x /= count_points
            point_y /= count_points
            pygame.draw.circle(self.screen, setting.MIDDLE_COLOR, (point_x, point_y), setting.RADIUS_DRONE)
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f"{camera.get_power_of_poi(drone)}", True,
                          (180, 0, 0))
        self.screen.blit(text1, (10, 0))
        text2 = f1.render(f"{drone.angle}", True,
                          (180, 0, 0))
        self.screen.blit(text2, (10, 20))

        self.clock.tick(setting.FPS)
        pygame.display.flip()
