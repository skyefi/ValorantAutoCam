#OCR scanning by Dornu Inene
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from tkinter import *

playerCams: dict[str, int]

#Point pytesseract to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = Tk()

root.title("Valorant Auto-Camera Setup")
root.geometry('450x200')

title = Label(root, text = "Enter player names and cameras\n")
title.grid(row=0)

p1Prompt1 = Label(root, text = "Player 1 - Username:")
p1Prompt1.grid(column=0,row=1)

user1tk = Entry(root)
user1tk.grid(column=1,row=1)

p1Prompt2 = Label(root, text = "  Camera: ")
p1Prompt2.grid(column=2,row=1)

cam1tk = Entry(root, width=5)
cam1tk.grid(column=3,row=1)

p2Prompt1 = Label(root, text = "Player 2 - Username:")
p2Prompt1.grid(column=0,row=2)

user2tk = Entry(root)
user2tk.grid(column=1,row=2)

p2Prompt2 = Label(root, text = "  Camera: ")
p2Prompt2.grid(column=2,row=2)

cam2tk = Entry(root, width=5)
cam2tk.grid(column=3,row=2)

p3Prompt1 = Label(root, text = "Player 3 - Username:")
p3Prompt1.grid(column=0,row=3)

user3tk = Entry(root)
user3tk.grid(column=1,row=3)

p3Prompt2 = Label(root, text = "  Camera: ")
p3Prompt2.grid(column=2,row=3)

cam3tk = Entry(root, width=5)
cam3tk.grid(column=3,row=3)

p4Prompt1 = Label(root, text = "Player 4 - Username:")
p4Prompt1.grid(column=0,row=4)

user4tk = Entry(root)
user4tk.grid(column=1,row=4)

p4Prompt2 = Label(root, text = "  Camera: ")
p4Prompt2.grid(column=2,row=4)

cam4tk = Entry(root, width=5)
cam4tk.grid(column=3,row=4)

p5Prompt1 = Label(root, text = "Player 5 - Username:")
p5Prompt1.grid(column=0,row=5)

user5tk = Entry(root)
user5tk.grid(column=1,row=5)

p5Prompt2 = Label(root, text = "  Camera: ")
p5Prompt2.grid(column=2,row=5)

cam5tk = Entry(root, width=5)
cam5tk.grid(column=3,row=5)

def camsParse(inputStr: str) -> int:
    num: int
    try:
        num = int(inputStr)
    except ValueError as valEr:
        num = -1
    return num

def infoSaved():
    global playerCams
    playerCams = {
        "": -1
    }
    
    playerCams[user1tk.get().lower()] = camsParse(cam1tk.get())
    playerCams[user2tk.get().lower()] = camsParse(cam2tk.get())
    playerCams[user3tk.get().lower()] = camsParse(cam3tk.get())
    playerCams[user4tk.get().lower()] = camsParse(cam4tk.get())
    playerCams[user5tk.get().lower()] = camsParse(cam5tk.get())
    
    playerCams.pop("")
                                
    root.destroy()

enter = Button(root, text="Save", command=infoSaved)
enter.grid(column = 3,row=7)

root.mainloop()


#############################################


print(playerCams)
#Runs until it hears "Esc"
changeCamFlag: bool = False
activeCam: int = -1
activePlayer: str = ""

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

            

cv2.destroyAllWindows()