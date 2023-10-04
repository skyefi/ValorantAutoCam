#OCR scanning by Dornu Inene
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from tkinter import *

import playerCamsInput
import atemControl

useAtem: bool = True
ipAddress: str = "128.175.81.250"
defaultCam: int = 5
useOBS: bool = False
readNames = ["/"," "," "]


#Point pytesseract to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


playerCams: dict[str, int] = playerCamsInput.getPlayerCams()
print(playerCams)

changeCamFlag: bool = False
activeCam: int = -1
activePlayer: str = ""

if useAtem:
    switcher = atemControl.Switcher(ipAddress, defaultCam)
    
if useOBS:
    import obsValScript as obs

#Runs until it hears "Esc"
while True:
    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break
    
    #Grabs image from (x1, y1) to (x2, y2)
    cap = ImageGrab.grab(bbox=(80, 1050, 500, 1250))

    #Optional, display image
    #cap_arr = np.array(cap)
    #cv2.imshow("", cap_arr)
    
    #Image to string conversion
    userText: str = pytesseract.image_to_string(cap)
    userText = userText.strip().replace("\n","").lower()

    # If any text was translated from the image, print it
    if len(userText) <= 0:
        continue
    
    playerInList: bool = False
    
    for p in playerCams.keys():
        if p in userText:
            if playerCams[p] != activeCam:
                activePlayer = p
            playerInList = True
            break
    
    if not playerInList:
        activePlayer = " "
    
    readNames[2] = readNames[1]
    readNames[1] = readNames[0]
    readNames[0] = activePlayer
    
    if readNames[2] == readNames[1] and readNames[1] == readNames[0]:
        if readNames[0] == " " and activeCam != -1:
            activeCam = -1
        elif readNames[0] != " ":
            activeCam = playerCams[activePlayer]
        changeCamFlag = True
    
    if changeCamFlag:
        print("New Cam! ActiveCam = " + str(activeCam) + " Player = " + activePlayer)
        changeCamFlag = False
        if useAtem:
            noCam: bool = switcher.switchCam(activeCam)
            if useOBS and noCam:
                obs.noCam()
            elif useOBS:
                obs.Cam()


cv2.destroyAllWindows()