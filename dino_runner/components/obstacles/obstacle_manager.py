from random import randint
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if len(self.obstacles) == 0:
            small_cactus = randint(0, 1)
            if small_cactus == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300)) 
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS, 320))

        #if len(self.obstacles) == 0:
            #bird = randint(Y_POS_LARGE_DOWN, Y_POS_LARGE_UP)
            #if bird == 0:
                #self.obstacles.append(Bird(Y_POS_LARGE_DOWN))
            #else:
                #self.obstacles.append(Bird(Y_POS_LARGE_UP))

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
