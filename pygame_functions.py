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

    def get_keyboard(self, drone: classes.Drone):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        if keys[pygame.K_w]:
            drone.move(0, -1)
        elif keys[pygame.K_s]:
            drone.move(0, 1)
        elif keys[pygame.K_a]:
            drone.move(-1, 0)
        elif keys[pygame.K_d]:
            drone.move(1, 0)

    def update(self, drone: classes.Drone, camera: classes.Camera):
        self.screen.fill(setting.FIELD_COLOR)
        pygame.draw.circle(self.screen, setting.DRONE_COLOR, drone.get_position(), setting.RADIUS_DRONE)
        pygame.draw.circle(self.screen, setting.POI_COLOR, camera.get_position(), setting.RADIUS_POI)
        self.clock.tick(setting.FPS)
        pygame.display.flip()
