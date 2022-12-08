from dino_runner.components import obstacles
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    Y_POS_LARGE_DOWN = 310
    Y_POS_LARGE_UP = 350

    def __init__(self):
        self.image = BIRD[0]
        self.step_index = 0
        
    def update(self, game_spedd, obstacles):
        self.flying()
        super().update()  #game_speed, obstacles

    def flying(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.Y_POS_LARGE_DOWN, self.Y_POS_LARGE_UP))
