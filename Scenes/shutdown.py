from Scenes.scene import Scene

class Shutdown(Scene):
    def __init__(self):
        super().__init__(core, audio, video, input)
        self.should_draw = True

    def Dispose(self):
        pass

    def Update(self):
        pass

    def InputUpdate(self, k1, k2, k3, ku, kd, kl, kr, kp):
        if kp:
            self.core.Shutdown()
        if k3:
            from Scenes.MainMenu import MainMenu
            self.core.ChangeScene(MainMenu)

    def Draw(self):
        if self.should_draw:
            self.video.DrawLargeText(None, (0, 0), "Shutdown?")
