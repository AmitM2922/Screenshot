from tkinter import *
import pyautogui
from tkinter.filedialog import*

amit=Tk()
amit.geometry("40x40+700+200")
amit.title("Screenshot By Amit Mulmule")

# For Taking  Screnshot...
def takeScreenShot():
    Mulmule=pyautogui.screenshot() # " Pyautogui.screenshot ye pyautogui me hota he "
    save_path=asksaveasfilename()
    Mulmule.save(save_path+"_screenshot.jpg")

 #for capture button..

sumit=Button(amit,text="Capture",bg="black",fg="red",command=takeScreenShot,relief=GROOVE,border=8,font=('bold',15),activebackground='pink')
sumit.pack(expand=True,fill='both')
    

amit.mainloop()
