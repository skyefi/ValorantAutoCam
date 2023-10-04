import PyATEMMax

class Switcher:
    def __init__(self, ipAddress: str, defaultCam: int):
        self._atem = PyATEMMax.ATEMMax()
        self._ip: str = ipAddress
        self._defaultCam: int = defaultCam
        
        self._atem.connect(ipAddress)
        self._atem.waitForConnection()

    def switchCam(self, cam: int) -> bool:
        if(cam > 0 and cam < 9):
            self._atem.setProgramInputVideoSource(0, cam)
            return True
        else:
            self._atem.setProgramInputVideoSource(0, self._defaultCam)
            return False
