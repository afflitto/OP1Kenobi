import os

from luma.core.render import canvas
from PIL import Image, ImageDraw, ImageFont

class Video:
    screen = None
    largeFont = None
    smallFont = None

    def __init__(self, width, height, fontFile, largeFontSize, smallFontSize):
        print('Video:: Starting Init ' + str(width) + ' ' + str(height))
        Video.buf = Image.new('1', (width, height))
        Video.large_font = ImageFont.truetype(fontFile, size=largeFontSize)
        Video.small_font = ImageFont.truetype(fontFile, size=smallFontSize)

    def Update(self):
        if Video.device:
            with canvas(Video.device) as draw:
                draw.bitmap((0, 0), Video.buf, fill="white")

    def DrawLargeText(self, color, position, text):
        dctx = ImageDraw.Draw(Video.buf)
        size = dctx.textsize(text, font=Video.large_font)
        dctx.text(position, text, fill="white", font=Video.large_font)
        del dctx
        return size

    def textsize(self, text):
        dctx = ImageDraw.Draw(Video.buf)
        size = dctx.textsize(text, font=Video.large_font)
        del dctx
        return size

    def DrawSmallText(self, color, position, text):
        dctx = ImageDraw.Draw(Video.buf)
        dctx.text(position, text, fill="white", font=Video.small_font)
        del dctx

    def FillScreen(self, color):
        Video.buf = Image.new('1', Video.buf.size)
