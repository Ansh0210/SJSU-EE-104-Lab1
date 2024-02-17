"""
Created on Tues Aug 29 15:27:41 2023

@author: Edwin Kulakkattolikel

Reference: https://www.geeksforgeeks.org/python-simple-calculator-using-tkinter/?ref=rp
"""

# importing Tkinter and math
#!pip install tkinter
from tkinter import *
import math

# calc class
class calc:

	def getandreplace(self):
		"""replace x with * and ÷ with /"""
		self.expression = self.e.get()
		self.newtext=self.expression.replace('/','/')
		self.newtext=self.newtext.replace('x','*')

	def equals(self):
		"""when the equal button is pressed"""
		self.getandreplace()
		try:
			# evaluate the expression using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)

	def squareroot(self):
		"""squareroot method"""
		self.getandreplace()
		try:
			# evaluate the expression using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqrtval=math.sqrt(self.value)
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def square(self):
		"""square method"""
		self.getandreplace()
		try:
			#evaluate the expression using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqval=math.pow(self.value,2)
			self.e.delete(0,END)
			self.e.insert(0,self.sqval)

##################################################################################
#square root of the inputted number
##################################################################################
	def squareRoot(self):
		"""squareRoot method"""
		self.getandreplace()
		try:
			#evaluate the expression using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.thirdval=math.pow(self.value,0.5)
			self.e.delete(0,END)
			self.e.insert(0,self.thirdval)

##################################################################################
#1/x of the inputted number
##################################################################################
	def inversePower(self):
		"""inversePower method"""
		self.getandreplace()
		try:
			#evaluate the expression using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.thirdval=math.pow(self.value,-1)
			self.e.delete(0,END)
			self.e.insert(0,self.thirdval)

	def clearall(self):
			"""when clear button is pressed,clears the text input area"""
			self.e.delete(0,END)

	def clear1(self):
			self.txt=self.e.get()[:-1]
			self.e.delete(0,END)
			self.e.insert(0,self.txt)

	def action(self,argi):
			"""pressed button's value is inserted into the end of the text area"""
			self.e.insert(END,argi)

##################################################################################
# renamed calculator name
##################################################################################
	def __init__(self,master):
			"""Constructor method"""
			master.title('Calculator')
			master.geometry()
			self.e = Entry(master)
			self.e.grid(row=0,column=0,columnspan=24,pady=10)
			self.e.focus_set() #Sets focus on the input text area

##################################################################################
# reordered button layout, changed colors, button sizes, changed button types
##################################################################################
			# Generating Buttons
			Button(master,text="%",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('%')).grid(row=1, column=0)
            
			Button(master,text="(",width=3,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('(')).grid(row=1, column=1, sticky = W)
            
			Button(master,text=")",width=3,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action(')')).grid(row=1, column=1, sticky = E)
            
			Button(master,text='AC',width=7,height=3,
				fg="white", bg="black",font='24',
			    command=lambda:self.clearall()).grid(row=1, column=2)
            
			Button(master,text='⌫',width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.clear1()).grid(row=1, column=3)
            
			Button(master,text="1/x",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.inversePower()).grid(row=2, column=0)
            
			Button(master,text="x²",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.square()).grid(row=2, column=1)
            
			Button(master,text="√x",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.squareRoot()).grid(row=2, column=2)
            
			Button(master,text="÷",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('/')).grid(row=2, column=3)
            
			Button(master,text="7",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action('7')).grid(row=3, column=0)
            
			Button(master,text="8",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(8)).grid(row=3, column=1)
            
			Button(master,text="9",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(9)).grid(row=3, column=2)
            
			Button(master,text="x",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('x')).grid(row=3, column=3)
            
			Button(master,text="4",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(4)).grid(row=4, column=0)
            
			Button(master,text="5",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(5)).grid(row=4, column=1)
            
			Button(master,text="6",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(6)).grid(row=4, column=2)
            
			Button(master,text="-",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('-')).grid(row=4, column=3)
            
			Button(master,text="1",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(1)).grid(row=5, column=0)
            
			Button(master,text="2",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(2)).grid(row=5, column=1)
            
			Button(master,text="3",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(3)).grid(row=5, column=2)
            
			Button(master,text="+",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('+')).grid(row=5, column=3)
            
			Button(master,text=".",width=7,height=3,
				fg="white",bg="black",font='24',
				command=lambda:self.action('.')).grid(row=6, column=0)
            
			Button(master,text="0",width=7,height=3,
				fg="black",bg="grey",font='24',
				command=lambda:self.action(0)).grid(row=6, column=1)
            
			Button(master,text="=",width=15,height=3,
                fg="black",bg="orange",font='24',
                command=lambda:self.equals()).grid(row=6, column=2,columnspan=2)

# Driver Code
root = Tk()

obj=calc(root) # object instantiated

root.mainloop()
