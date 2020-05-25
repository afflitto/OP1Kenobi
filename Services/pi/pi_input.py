import RPi.GPIO as GPIO

from Services.common.Input import Input, Key
from Config import Config

class PiInput(Input):
    def __init__(self):
        self.key_map = {
            Config.KeyLeftPin: Key.KEY_LEFT,
            Config.KeyRightPin: Key.KEY_RIGHT,
            Config.KeyUpPin: Key.KEY_UP,
            Config.KeyDownPin: Key.KEY_DOWN,
            Config.KeyPressPin: Key.KEY_PRESS,
            Config.Key1Pin: Key.KEY_1,
            Config.Key2Pin: Key.KEY_2,
            Config.Key3Pin: Key.KEY_3,
        }
        self.pressed_key: Key = None
        GPIO.setup(Config.KeyLeftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.KeyRightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.KeyUpPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.KeyDownPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.KeyPressPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.Key1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.Key2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Config.Key3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(Config.KeyLeftPin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.KeyRightPin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.KeyUpPin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.KeyDownPin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.KeyPressPin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.Key1Pin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.Key2Pin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)
        GPIO.add_event_detect(Config.Key3Pin, GPIO.FALLING, self.detect_callback, bouncetime=Config.BounceTime)

    def Update(self):
        pass

    def detect_callback(self, pin):
        self.pressed_key = self.key_map[pin]

    def KeyDown(self, key: Key):
        if key == self.pressed_key:
            self.pressed_key = None
            return True
        return False
