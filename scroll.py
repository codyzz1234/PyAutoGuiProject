import pyautogui
import time

time.sleep(1)
while True:
    try:
        thumbNailX,thumbNailY = pyautogui.locateCenterOnScreen(r"C:\Users\kenle\Desktop\PyAutoGuiProject\UploadThumbNailButton.png",confidence=.9) #SS the UploadThumnailButton then put the directory to it here
        pyautogui.click(thumbNailX,thumbNailY)
        print("trying")
    except Exception as e:
        print("error")
        pyautogui.scroll(-500)
        time.sleep(1)
        continue
    else:
        print("Done")
        break;
    
time.sleep(1.5)
pyautogui.write("BillyHerrington") #FileNameHere
pyautogui.press('enter')
    
# pyautogui.scroll(-300)
# thumbNailX,thumbNailY = pyautogui.locateCenterOnScreen(r"C:\Users\kenle\Desktop\PyAutoGuiProject\UploadThumbNailButton.png")
# pyautogui.click(thumbNailX,thumbNailY)
# pyautogui.write("ImageFileName")