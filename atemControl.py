import PyATEMMax

class Switcher:
    def __init__(self, ipAddress: str):
        self._atem = PyATEMMax.ATEMMax()
        self._ip: str = ipAddress
        
        self._atem.connect(ipAddress)
        self._atem.waitForConnection()

    def switchCam(self, cam: int):
        if(cam > 0 and cam < 9):
            self._atem.setProgramInputVideoSource(0, cam)
        else:
            #Tell OBS to remove the cam
            #but for now, use Cam 8
            self._atem.setProgreamInputVideoSource(0, 8)
