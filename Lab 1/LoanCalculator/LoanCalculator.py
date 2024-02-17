# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:56:49 2020
Author: Shivansh Shukla

Reference: https://www.geeksforgeeks.org/python-loan-calculator-using-tkinter/?ref=rp
"""
# Import tkinter
from tkinter import *
class LoanCalculator:

    def __init__(self):

        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        
        # create the input boxes.
        Label(window, text = "Annual Interest Rate (%)").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        #Label(window, text = "Number of Months").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Loan Amount ($)").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Monthly Payment ($)").grid(row = 4, column = 1, sticky = W)
        
        #creat new label for total interest
        Label(window, text = "Total Payment ($)").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Total Interest Paid ($)").grid(row = 6, column = 1, sticky = W) 
        
        # for taking inputs
        self.annualInterestRateVar = StringVar() #construct input string
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2) # take user input 
        
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
        
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)

        self.totalPaymentVar = StringVar() # total payment label 
        Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)
        
        self.interest_paid = StringVar() #interest paid label
        Label(window, textvariable= self.interest_paid).grid(row = 6, column = 2, sticky = E) # label the interest paid in the column

        # create the button
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 7, column = 2, sticky = E)
        window.mainloop() # Create an event loop

    # compute the total payment.
    def computePayment(self):

        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.numberOfYearsVar.get())
        )
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
        
        total_interest_paid = self.get_interest_paid(totalPayment, float(self.loanAmountVar.get())) # calculate total interest paid
        self.interest_paid.set(format(total_interest_paid, '10.2f')) # set the varibale to the value
        

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment. 
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 
            1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        #root = Tk() # create the widget
    
    # func to find total interest paid   
    def get_interest_paid(self, totalPayment, loanAmount):
        # compute interest paid
        interest_paid = totalPayment - loanAmount
        return interest_paid
        

# call the class to run the program.
LoanCalculator()
