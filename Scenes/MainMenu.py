# resources
from Config import *
from Resources.Colors import *

# services
from Services.common.Core import *
from Services.common.Video import Video
# from Services.Input import *

from Scenes.menu import Menu, MenuEntry
from Scenes.Samples import Samples
from Scenes.Backups import Backups
from Scenes.ManageFiles import ManageFiles
from Scenes.shutdown import Shutdown



class MainMenu(Menu):
    def __init__(self, core, audio, video, input):
        print('MainMenu:: Starting Init')
        super().__init__(core, audio, video, input)
        self.g = 0

        self.menu_entries = [
            MenuEntry('Browse Sounds', Samples), #Samples
            MenuEntry('Backups', Backups), #Backups
            MenuEntry('Manage Files', ManageFiles), #ManageFiles
            MenuEntry('Shutdown', Shutdown),
        ]

        self.menu_entries[0].is_selected = True

    def Dispose(self):
        pass

    def Update(self):
        self.g = self.g + 1
        if (self.g > 255):
            self.g = 0

    def SelectMenuEntry(self, menu_entry:MenuEntry):
        self.core.ChangeScene(menu_entry.action)
