import pygame
from typing import Dict
from Services.common.Input import Input, Key

class PCInput(Input):

    def __init__(self):
        print("init pc input")
        self.key_map = {
            pygame.K_LEFT: Key.KEY_LEFT,
            pygame.K_RIGHT: Key.KEY_RIGHT,
            pygame.K_UP: Key.KEY_UP,
            pygame.K_DOWN: Key.KEY_DOWN,
            pygame.K_RETURN: Key.KEY_PRESS,
            pygame.K_KP1: Key.KEY_1,
            pygame.K_KP2: Key.KEY_2,
            pygame.K_KP3: Key.KEY_3,
        }
        self.pressed_key: Key = None

    def Update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_map:
                    self.pressed_key = self.key_map[event.key]
                    return

    def KeyDown(self, key: Key):
        if key == self.pressed_key:
            self.pressed_key = None
            return True
        return False
