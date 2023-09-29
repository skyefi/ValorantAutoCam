#OCR scanning by Dornu Inene
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from tkinter import *

import playerCamsInput
import atemControl

debug: bool = False
ipAddress: str = "192.1.1.1"


#Point pytesseract to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


playerCams: dict[str, int] = playerCamsInput.getPlayerCams()
print(playerCams)

changeCamFlag: bool = False
activeCam: int = -1
activePlayer: str = ""

if not debug:
    switcher = atemControl.Switcher(ipAddress)

#Runs until it hears "Esc"
while True:
    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break
    
    #Grabs image from (x1, y1) to (x2, y2)
    cap = ImageGrab.grab(bbox=(50, 850, 300, 950))

    #Optional, display image
    cap_arr = np.array(cap)
    cv2.imshow("", cap_arr)
    
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
                changeCamFlag = True
                activeCam = playerCams[p]
                activePlayer = p
            playerInList = True
            break
    
    print(playerInList)
    if not playerInList:
        if activeCam != -1:
            changeCamFlag = True
            activeCam = -1
            activePlayer = ""
    
    if changeCamFlag:
        print("New Cam! ActiveCam = " + str(activeCam))
        changeCamFlag = False
        if not debug: switcher.switchCam(activeCam)

            

cv2.destroyAllWindows()