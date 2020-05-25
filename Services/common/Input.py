from enum import Enum

class Key(Enum):
    KEY_1 = 1
    KEY_2 = 2
    KEY_3 = 3
    KEY_UP = 4
    KEY_DOWN = 5
    KEY_LEFT = 6
    KEY_RIGHT = 7
    KEY_PRESS = 8


class Input():
    def Update(self):
        pass

    def KeyDown(self, keyPin):
        pass
