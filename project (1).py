# importing all libraries

from tkinter import *                        #GUI
from timeit import default_timer as timer
import random


window = Tk()


window.geometry("760x300+100+20")
window.title('Tpying Speed Test')
window.configure(bg='olive')

x = 0                                        #global variable

def game():
	global x
	
	
	if x == 0:
		window.destroy()
		x +=1

	def check_result():
	
		if paragraphEntry.get() == paragraphs[paragraph]:
           
			end = timer()

			print(end-start)
	
		else:
			print("Wrong Input")

	paragraphs = ['this is a python program','technology is best when it brings people together',
	        'i used tkinter library in this project','typing speed test by python',
			'fear is a reaction but courage is a decision','we are changing the world with technology',
			'cloud computing is the third wave of digital revolution','#include<stdio.h>',
			'#include<conio.h>','printf("this is a python program");','scanf("%d",& arr[a]);',
			'for(a=0;a>=10;a++)','cout<<"hellow myself manish kumar";','#include<iostream.h>',
			'cout<<sum of total number<<a+b+c;','if(arr[d]==y)']

	paragraph = random.randint(0, (len(paragraphs)-1))

	windows = Tk()			
	start = timer()                    
	windows.geometry("760x300+100+20")
	windows.title('Tpying Speed Test')
	windows.configure(bg='olive')

	wordLabel = Label(windows, text=paragraphs[paragraph], font=('airal',16,'italic bold'),
                                bg='olive',fg='white')
	wordLabel.place(x=200, y=50)
	
	fontLabel2 = Label(windows, text="Start Typing",font=('airal',25,'italic bold'),
                                bg='olive',fg='black')
	fontLabel2.place(x=10, y=0)

	paragraphEntry = Entry(windows,font=('airal',16,'italic bold'),bd=5)
	paragraphEntry.place(x=200, y=100)
	paragraphEntry.focus_set()                           
	

	doneButton = Button(windows, text="Done",command=check_result, width=12,
	                       font=('airal',12,'italic bold') ,bg='blue',fg='white')
	doneButton.place(x=200, y=160)

	tryagainButton = Button(windows, text="Try Again",command=game, width=12,
							font=('airal',12,'italic bold') ,bg='blue',fg='white')
	tryagainButton.place(x=340, y=160)
	windows.mainloop()



fontLabel = Label(window, text="Lets start playing..", font=('airal',30,'italic bold'),
                            bg='olive',fg='black')
fontLabel.place(x=10, y=20)     

goButton = Button(window, text="Go", command=game,width=6,font=('airal',22,'italic bold'),
                             bg='blue',fg='white')
goButton.place(x=300, y=120)


window.mainloop()     



















