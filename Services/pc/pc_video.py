import os

from luma.core.render import canvas
from luma.emulator.device import pygame

from Services.common.Video import Video

class PCVideo(Video):
    screen = None
    largeFont = None
    smallFont = None

    def __init__(self, width, height, fontFile, largeFontSize, smallFontSize):
        Video.device = pygame(width=width, height=height, mode="1")
        super().__init__(width, height, fontFile, largeFontSize, smallFontSize)
