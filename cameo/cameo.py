#!/usr/bin/python3
import cv2
from managers import WindowManager,CaptureManager
import filters

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture("/dev/video0"),self._windowManager,True)

    def run(self):
        """run the main loop"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            # TODO:Filter the framea
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self,keycode):
        """
        Handle a keypress

        space   ->  Take a screenshot.
        tab     ->  Start/Stop video record
        escape  ->  Quit

        """
        if keycode == 32:   #space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: #quit
            self._windowManager.destoryWindow()

if __name__ == "__main__":
    Cameo().run()
