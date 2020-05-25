from abc import ABC, abstractmethod
from typing import Any

from Scenes.scene import Scene
from Config import Config

class MenuEntry:
    def __init__(self, text: str, action: Any):
        self.text = text
        self.is_selected = False
        self.action = action

class Menu(Scene, ABC):
    def __init__(self, core, audio, video, input):
        super().__init__(core, audio, video, input)
        self.menu_entries: List[MenuEntry] = []
        self.current_index = 0
        self.scroll_index_offset = 0
        self.selected_off_screen = False

    @abstractmethod
    def Dispose(self):
        raise NotImplementedError()

    @abstractmethod
    def Update(self):
        raise NotImplementedError()

    @abstractmethod
    def SelectMenuEntry(self):
        raise NotImplementedError()

    def GoBack(self):
        from Scenes.MainMenu import MainMenu
        self.core.ChangeScene(MainMenu)

    def ChangeMenuIndex(self, delta):
        self.current_index += delta
        if len(self.menu_entries) > 0:
            self.current_index %= len(self.menu_entries)

        for i in range(0, len(self.menu_entries)):
            if i == self.current_index:
                self.menu_entries[i].is_selected = True
            else:
                self.menu_entries[i].is_selected = False

    def InputUpdate(self, k1, k2, k3, ku, kd, kl, kr, kp):
        if (ku):
            self.ChangeMenuIndex(-1)
        elif (kd):
            self.ChangeMenuIndex(1)
        if k3:
            self.GoBack()
        if (k1 or kp):
            self.SelectMenuEntry(self.menu_entries[self.current_index])

    def Draw(self):
        #TODO: scrolling is kinda just hacked together so this should be improved
        indexColor = (100, self.g, 100)
        draw_y = 0

        for i in range(0, len(self.menu_entries)):
            _, height = self.video.textsize(self.menu_entries[i].text)
            if self.menu_entries[i].is_selected:
                marker = '>'
                if draw_y + height - self.scroll_index_offset > Config.DisplayHeight:
                    self.scroll_index_offset = height - Config.DisplayHeight + draw_y
                if draw_y - self.scroll_index_offset < 0:
                    self.scroll_index_offset = draw_y
            else:
                marker = ' '

            text = f"{marker}{self.menu_entries[i].text}"
            self.video.DrawLargeText(None, (0, draw_y - self.scroll_index_offset), text)
            draw_y += height
