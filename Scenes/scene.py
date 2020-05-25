from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, core, audio, video, input):
        self.core = core
        self.audio = audio
        self.video = video
        self.input = input

    @abstractmethod
    def Dispose(self):
        raise NotImplementedError()

    @abstractmethod
    def Update(self):
        raise NotImplementedError()

    @abstractmethod
    def InputUpdate(self, k1, k2, k3, ku, kd, kl, kr, kp):
        raise NotImplementedError()

    @abstractmethod
    def Draw(self):
        raise NotImplementedError()
