from random import randint
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacles.bird import Y_POS_LARGE_DOWN
from dino_runner.components.obstacles.bird import Y_POS_LARGE_UP


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = randint(0, 5)
            if obstacle_type == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300)) 
            elif obstacle_type == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS, 320))
            else:
                bird = randint(0, 1)
                if bird == 0:
                    self.obstacles.append(Bird(Y_POS_LARGE_DOWN))
                else:
                    self.obstacles.append(Bird(Y_POS_LARGE_UP))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            obstacle.rect.colliderect
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False 
                game.death_count += 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
