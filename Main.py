# system imports
import sys
import time,os,datetime
import shutil as sh

# resources
from Config import *
from Resources.Colors import *

# services
from Services.common.Audio import *
from Services.common.Core import *
from Services.common.Input import Key
#
# from Services.pc.pc_video import PCVideo
# from Services.pc.pc_input import PCInput
from Services.pi.pi_input import PiInput
from Services.pi.pi_video_sh1106 import PiVideoSH1106

# scenes
from Scenes.MainMenu import *

# initialize
print('Main:: Starting Init')
core = Core()

video = PiVideoSH1106(
    Config.DisplayWidth,
    Config.DisplayHeight,
    Config.FontFile,
    Config.LargeFontSize,
    Config.SmallFontSize)
audio = Audio(core)
input = PiInput()

# video = PCVideo(
#     Config.DisplayWidth,
#     Config.DisplayHeight,
#     Config.FontFile,
#     Config.LargeFontSize,
#     Config.SmallFontSize
# )
# audio = Audio(core)
# input = PCInput()


def Main():
    print('Main:: Starting Main')
    global core
    global video
    global audio
    global input

    core.RegisterServices(video, audio, input)
    core.ChangeScene(MainMenu)
    lastDisplayUpdateTime = 0
    lastInputUpdateTime = 0
    core.running = True

    while core.running:
        core.Update()
        core.currentScene.Update()

        if (core.GetTime() - lastDisplayUpdateTime > Config.DisplayUpdateSpeed):
            lastDisplayUpdateTime = core.GetTime()
            video.FillScreen(Colors.Black)
            core.currentScene.Draw()

        if (core.GetTime() - lastInputUpdateTime > Config.InputUpdateSpeed):
            lastInputUpdateTime = core.GetTime()
            core.currentScene.InputUpdate(
                input.KeyDown(Key.KEY_1),
                input.KeyDown(Key.KEY_2),
                input.KeyDown(Key.KEY_3),
                input.KeyDown(Key.KEY_UP),
                input.KeyDown(Key.KEY_DOWN),
                input.KeyDown(Key.KEY_LEFT),
                input.KeyDown(Key.KEY_RIGHT),
                input.KeyDown(Key.KEY_PRESS),
            )

        video.Update()
        audio.Update()
        input.Update()

def Intro():
    print('Main:: Starting Intro')
    global core
    global video
    global audio

    # TODO: Intro screen

if __name__ == '__main__':
    Intro()
    Main()
    pygame.quit()
    sys.exit()
