import tkinter
import cv2
import tkinter.messagebox
import tkinter.ttk
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk
import os

class MyWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Gray Scale")
        self.geometry("1000x800")
        self.config(background="dark gray")
        self.nameLabel=tkinter.Label(master=self,text="Convert to GrayScale : ",font="Verdana 12 bold",fg="black",bg="light yellow")
        self.nameLabel.place(x=25,y=50)
        self.openButton=tkinter.Button(master=self,text="Open",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.openFile,relief="solid")
        self.openButton.place(x=50,y=100)
        self.saveButton=tkinter.Button(master=self,text="Save",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.saveFile,relief="solid")
        self.saveButton.place(x=200,y=100)
        self.maxButton=tkinter.Button(master=self,text="Max",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.maxFile,relief="solid")
        self.maxButton.place(x=350,y=100)
        self.minButton=tkinter.Button(master=self,text="Min",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.minFile,relief="solid")
        self.minButton.place(x=500,y=100)
        self.avgButton=tkinter.Button(master=self,text="Average",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.avgFile,relief="solid")
        self.avgButton.place(x=650,y=100)
        self.lumButton=tkinter.Button(master=self,text="Luminosity",fg="red",bg="yellow",width=10,padx=5,pady=3,command=self.lumFile,relief="solid")
        self.lumButton.place(x=800,y=100)
        self.brightnessSlider=Scale(self,from_=-255,to=255,orient=HORIZONTAL,fg="red",bg="yellow",command=self.brightness,resolution=50)
        self.brightnessSlider.set(0)
        self.brightnessSlider.place(x=50,y=150)
        self.contrastSlider=Scale(self,from_=-255,to=255,orient=HORIZONTAL,fg="red",bg="yellow",command=self.contrast,resolution=50)
        self.contrastSlider.set(0)
        self.contrastSlider.place(x=200,y=150)
        self.file=""
        self.imageData=""

    def openFile(self):
        self.file=askopenfilename()
        load=Image.open(self.file)
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def saveFile(self):
        filename=asksaveasfilename()    
        cv2.imwrite(filename,self.imageData)

    def maxFile(self):
        self.imageData=cv2.imread(self.file)
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=int(rgb[0])
                green=int(rgb[1])
                blue=int(rgb[2])
                if red>green: clr=red
                else: clr=green
                if clr<blue: clr=blue
                self.imageData[r][c]=(clr,clr,clr)
        cv2.imwrite("maxFile.jpg",self.imageData)
        load=Image.open("maxFile.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def minFile(self): 
        self.imageData=cv2.imread(self.file)
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=int(rgb[0])
                green=int(rgb[1])
                blue=int(rgb[2])
                if red<green: clr=red
                else: clr=green
                if clr>blue: clr=blue
                self.imageData[r][c]=(clr,clr,clr)
        cv2.imwrite("minFile.jpg",self.imageData)
        load=Image.open("minFile.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def avgFile(self):
        self.imageData=cv2.imread(self.file)
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=int(rgb[0])
                green=int(rgb[1])
                blue=int(rgb[2])
                avg=int((red+green+blue)/3)
                self.imageData[r][c]=(avg,avg,avg)
        cv2.imwrite("avgFile.jpg",self.imageData)
        load=Image.open("avgFile.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def brightness(self,brightness):
        self.imageData=cv2.imread(self.file)
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=rgb[2]
                green=rgb[1]
                blue=rgb[0]
                red+=int(brightness)
                green+=int(brightness)
                blue+=int(brightness)
                if red>255: red=255
                if red<0: red=0
                if green>255: green=255
                if green<0: green=0
                if blue>255: blue=255
                if blue<0: blue=0
                self.imageData[r][c]=(blue,green,red)
        cv2.imwrite("brightness.jpg",self.imageData)
        load=Image.open("brightness.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def contrast(self,contrast):
        self.imageData=cv2.imread(self.file)
        f=(259*(int(contrast)+255))/(255*(259-int(contrast)))
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=rgb[2]
                green=rgb[1]
                blue=rgb[0]
                newRed=(f*(red-128))+128
                newGreen=(f*(red-128))+128
                newBlue=(f*(red-128))+128
                if newRed>255: newRed=255
                if newRed<0: newRed=0
                if newGreen>255: newGreen=255
                if newGreen<0: newGreen=0
                if newBlue>255: newBlue=255
                if newBlue<0: newBlue=0
                self.imageData[r][c]=(newBlue,newGreen,newRed)
        cv2.imwrite("contrast.jpg",self.imageData)
        load=Image.open("contrast.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

    def lumFile(self):
        self.imageData=cv2.imread(self.file)
        for r in range(self.imageData.shape[0]):
            for c in range(self.imageData.shape[1]):
                rgb=self.imageData[r][c]
                red=(int(rgb[0])*0.11)
                green=(int(rgb[1])*.59)
                blue=(int(rgb[2])*.3)
                total=red+green+blue
                self.imageData[r][c]=(total,total,total)
        cv2.imwrite("lumFile.jpg",self.imageData)
        load=Image.open("lumFile.jpg")
        load=load.resize((600,450),Image.ANTIALIAS)
        self.panel=ImageTk.PhotoImage(load)
        img=tkinter.ttk.Label(self,image=self.panel)
        img.image=self.panel
        img.place(x=200,y=250)

window=MyWindow()
window.mainloop()