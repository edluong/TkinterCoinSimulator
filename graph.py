from tkinter import *
from random import *
import time


class makeGraph:
		
	def __init__(self,master,wdth,hght):
		#set size of the window
		master.minsize(800,600)
		
		
		#Title of Program
		master.title("Coin Simulator V1")
		
		#Counters and variables
		self.headsCntr = IntVar()
		self.tailsCntr = IntVar()
		self.totalCntr = IntVar()
		self.probHeads= DoubleVar()
		self.probTails =  DoubleVar()
		self.headsHeight= 400
		self.tailsHeight = 400
			
		
		#create the frame that canvas will lay on
		self.frame = Frame(master,width=wdth,height=hght)
		self.frame.pack(expand=False,pady=40)
		self.frame.config(highlightthickness=1,highlightbackground="black")
		
		#create the canvas
		self.canvas = Canvas(self.frame,width=wdth,height=hght,bg="#F3EFE0")
		self.canvas.pack()
		
		#create the labels to be packed on top of the bar graphs
		#coordiates for this label should be (x1+x2 )/ 2 of bar graph 1
		labelHeads=self.canvas.create_text(187.5,0,text="Heads",justify=CENTER,anchor=N)
		labelTails=self.canvas.create_text(387.5,0,text="Tails",justify=CENTER,anchor=N)
		
		
		#create the counters for heads or tails
		self.labelHeadsCntr = self.canvas.create_text(187.5,15,text=self.getHeadsNum(),justify=CENTER,anchor=N)	  #inital (187.5,15)
		self.labelTailsCntr = self.canvas.create_text(387.5,15,text=self.getTailsNum(),justify=CENTER,anchor=N)		 #initial (387.5,15)
		
		#create the two initial bar graphs
		self.bRect = self.canvas.create_rectangle(150,400,225, 400,fill="#3399FF") #(150,30,225,400)
		self.gRect = self.canvas.create_rectangle(350,400,425, 400,fill="#217C7E") #(350,30,425,400)
		
		
		#create the second frame for buttons
		self.frameButtons = Frame(master)
		self.frameButtons.pack()
		
		self.buttonFlip= Button(self.frameButtons,text="Flip!")
		self.buttonFlip.config(width=30,height=4)
		self.buttonFlip.bind("<Button-1>",self.addOne)
		self.buttonFlip.pack(side=LEFT)
		
	
		self.buttonReset = Button(self.frameButtons,text="Reset")
		self.buttonReset.config(width=30,height=4)
		self.buttonReset.pack(side=LEFT)
		
	def addOne(self,event=None):
	
		#change the display of the info
		self.tempNum = round(random())
		if self.tempNum == 0:
			self.headsCntr.set(self.headsCntr.get()+1)
		else:
			self.tailsCntr.set(self.tailsCntr.get()+1)
		
		self.canvas.itemconfig(self.labelHeadsCntr,text=self.getHeadsNum())
		self.canvas.itemconfig(self.labelTailsCntr,text=self.getTailsNum())
		
		self.totalCntr.set(self.headsCntr.get()+self.tailsCntr.get())
		#change the physical height of the graphs
		if self.totalCntr.get()  > 0:
			self.probHeads.set(self.headsCntr.get() / self.totalCntr.get())
			self.probTails.set(self.tailsCntr.get() / self.totalCntr.get())
			#print(self.probHeads.get())
			self.canvas.coords(self.bRect,150,self.scale(self.probHeads.get()),225,400)
			self.canvas.coords(self.gRect,350,self.scale(self.probTails.get()),425,400)
			
			
		
		#used for testing the variables are changing, can disregard
		#print("heads: ",self.headsCntr.get())
		#print("tails: ",self.tailsCntr.get())
	
	def getHeadsNum(self):
		return self.headsCntr.get()
	
	def getTailsNum(self):
		return self.tailsCntr.get()
		
	def scale(self,prob):
		temp = 0
		if prob == 0:
			temp = 400
		elif prob == 1:
			temp = 30
		else:
			temp = 370-(370 * prob)
		return temp
			

			
root = Tk()
width = 600
height = 400
mG = makeGraph(root,width,height)

root.mainloop()