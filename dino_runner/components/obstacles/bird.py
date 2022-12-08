from pygame import Surface
from dino_runner.components import obstacles
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

Y_POS_LARGE_DOWN = 260
Y_POS_LARGE_UP = 310

class Bird(Obstacle):


    def __init__(self, pos):
        self.image = BIRD[0]
        self.step_index = 0
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = pos 

    def update(self, game_spedd, obstacles):
        self.flying()
        super().update(game_spedd, obstacles)  

    def flying(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1
        if self.step_index > 10:
            self.step_index = 0
        
    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))