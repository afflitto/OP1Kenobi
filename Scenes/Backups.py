from time import sleep

# resources
from Config import *
from Resources.Colors import *

# services
from Services.common.PhraseInput import *
from Scenes.menu import Menu, MenuEntry


class Backups(Menu):
    def loadDirectoryData(self, path):
        files, directories = self.core.GetDataInDirectory(path)
        self.currentDirectories = directories
        self.currentFiles = []
        self.currentIndex = 0
        self.contextPosition = 0
        self.backupSelection = 0

        for file in files:
            if ".aif" in file.lower():
                self.currentFiles.append(file)

    def getObjectType(self, index):
        if index < len(self.currentDirectories):
            return "Directory"
        elif (index - len(self.currentDirectories)) < len(self.currentFiles):
            return "File"
        else:
            return None

    def getObject(self, index):
        if index < len(self.currentDirectories):
            return self.currentDirectories[index]
        elif (index - len(self.currentDirectories)) < len(self.currentFiles):
            return self.currentFiles[(index - len(self.currentDirectories))]
        else:
            return None

    def __init__(self, core, audio, video, input):
        print('Backups:: Starting Init')

        super().__init__(core, audio, video, input)

        self.local = False
        self.menu = 0
        self.cursorPosition = 0
        self.g = 0
        self.currentIndex = 0
        self.volume = self.audio.GetVolume()
        self.phraseInput = PhraseInput()
        self.op1Present = self.core.IsUSBDeviceConnected(Config.OP1USBVendor, Config.OP1USBProduct)

        self.menu_entries = [
            MenuEntry('New Folder', "new_folder"),
            MenuEntry('All', "all"),
            MenuEntry('Synths', "synth"),
            MenuEntry('Drums', "drum"),
            MenuEntry('Tapes', "tape"),
            MenuEntry('Albums', "album"),
        ]

        self.menu_entries[0].is_selected = True

        if self.op1Present:
            # create mount directory if it doesn't exist
            self.core.ForceDirectory(Config.OP1USBMountDir)
            # get usb drive mount path
            self.mountpath = self.core.GetUSBMountPath(Config.OP1USBId)
            print(" > OP-1 device path: %s" % self.mountpath)
            # mount it!
            try:
                self.core.MountDevice(self.mountpath, Config.OP1USBMountDir)
            except:
                print("failed to mount device")
            # load contents
            self.loadDirectoryData(Config.MediaDirectory + "/" + Config.BackupDirectory + "/");

    def Dispose(self):
        pass

    def Update(self):
        self.g = self.g + 1
        if (self.g > 255):
            self.g = 0

    def SelectMenuEntry(self, menu_entry:MenuEntry):
        if menu_entry.action == "new_folder":
            self.menu = 1
        else:
            self.backupSelection = menu_entry.action
            self.menu = 2


    def CopyFiles(self):
        self.video.FillScreen(Colors.Black)
        self.video.DrawLargeText(
            Config.PrimaryTextColor,
            (30, 30),
            "Copying!")

        self.video.Update()

        if self.local:
            sourceDirectory = Config.MediaDirectory + "/" + Config.BackupDirectory + "/" + Config.BackupContext + "/"
            destinationDirectory = Config.OP1USBMountDir + "/"
        else:
            sourceDirectory = Config.OP1USBMountDir + "/"
            destinationDirectory = Config.MediaDirectory + "/" + Config.BackupDirectory + "/" + Config.BackupContext + "/"

        self.core.DeleteFolder(destinationDirectory + "synth")
        self.core.DeleteFolder(destinationDirectory + "drum")
        if self.backupSelection != "all":
            sourceDirectory += f"/{self.backupSelection}/"
            destinationDirectory += f"/{self.backupSelection}/"


        # copy
        print("All:: Copying data from")
        print(sourceDirectory)
        print("to")
        print(destinationDirectory)
        self.core.CopyFolder(sourceDirectory, destinationDirectory)
        self.menu = 0

    def SwitchContext(self):
        if self.local == True:
            self.local = False
        else:
            self.local = True

    def InputUpdate(self, k1, k2, k3, ku, kd, kl, kr, kp):
        if self.menu == 1:
            if k3:
                self.menu = 0
        elif self.menu == 2:
            if k1 or kp:
                self.CopyFiles()
            if k3:
                self.menu = 0
            if kr:
                print(self.video.large_font.size)
                self.video.large_font.size += 1
        else:
            super().InputUpdate(k1, k2, k3, ku, kd, kl, kr, kp)

    def CreateNewDirectory(self):
        # create new backup directory
        self.core.ForceDirectory(Config.MediaDirectory + "/" + Config.BackupDirectory + "/" + Config.BackupContext)

        # reload backup directories
        self.loadDirectoryData(Config.MediaDirectory + "/" + Config.BackupDirectory + "/")

        # select new backup directory
        for index, directory in enumerate(self.currentDirectories):
            if self.core.getNormPath(directory) == Config.BackupContext:
                self.contextPosition = index

        # back to backup main menu
        self.menu = 0

    def Draw(self):
        indexColor = (100, self.g, 100)

        if self.op1Present:
            if self.menu == 0:
                super().Draw()
            elif self.menu == 2:
                if self.local:
                    self.video.DrawLargeText(
                        Config.PrimaryTextColor,
                        (0, 0),
                        "Restore?")
                else:
                    self.video.DrawLargeText(
                        Config.PrimaryTextColor,
                        (0, 0),
                        "Backup?")

                width, _ = self.video.DrawLargeText(
                        Config.PrimaryTextColor,
                        (0, 32),
                        "Folder:")

                self.video.DrawLargeText(
                        Config.PrimaryTextColor,
                        (width + 5, 32),
                        Config.BackupContext)
        else:
            self.video.DrawLargeText(
                indexColor,
                (10, 10),
                "OP1 Drive")

            self.video.DrawLargeText(
                indexColor,
                (10, 25),
                "Not Present!")

            self.video.DrawSmallText(
                Config.PrimaryTextColor,
                (10, 40),
                "Return to the menu,")

            self.video.DrawSmallText(
                Config.PrimaryTextColor,
                (10, 48),
                "plug in the OP1")

            self.video.DrawSmallText(
                Config.PrimaryTextColor,
                (10, 56),
                "and try again.")
