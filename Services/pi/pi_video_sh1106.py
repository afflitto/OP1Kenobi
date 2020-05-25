import os

from luma.core.render import canvas
from luma.core.interface.serial import spi
from luma.oled.device import sh1106

from Services.common.Video import Video

class PiVideoSH1106(Video):
    screen = None
    largeFont = None
    smallFont = None

    def __init__(self, width, height, fontFile, largeFontSize, smallFontSize):
        Video.device = sh1106(spi(), width=width, height=height, mode="1", rotate=2)
        super().__init__(width, height, fontFile, largeFontSize, smallFontSize)
