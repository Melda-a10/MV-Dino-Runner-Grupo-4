import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HUMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE
from dino_runner.utils.text_utils import draw_message_component

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HUMMER_TYPE: DUCKING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HUMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HUMMER_TYPE: JUMPING_HAMMER}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.reset_dino_rect()
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.ducking = False
        self.has_power_up = False 
        self.shield = False
        self.shield_time_up = 0
        self.hummer = False
        self.hummer_time_up = 0
        self.show_text = False

    def update(self, user_input):
        if self.ducking:
            self.duck()
        elif self.jumping:
            self.jump()
        elif self.running:
            self.run()

        if user_input[pygame.K_UP] and not self.jumping:
            self.jumping = True 
            self.running = False
            self.ducking = False 
        elif not self.jumping:
            self.running = True 
            self.jumping = False 
            self.ducking = False 

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False 
            self.jumping = False 
        elif not self.jumping:
            self.running = True
        

    def run(self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1]
        self.reset_dino_rect()
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4 
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS 
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1]
        self.reset_dino_rect()
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1  
        
    def reset_dino_rect(self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        self.check_power_up(screen)

    def check_power_up(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2) 
            if time_to_show >= 0 and self.show_text:
                draw_message_component(
                    f"Shield enabled for: {time_to_show}",
                    screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.shield = False
                self.type = DEFAULT_TYPE

        if self.hummer:
            time_to_show = round((self.hummer_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0 and self.show_text:
                draw_message_component(
                    f"Hammer enabled for: {time_to_show}",
                    screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.hummer = False
                self.type = DEFAULT_TYPE
