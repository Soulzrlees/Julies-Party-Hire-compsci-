# importing the tkinter program 
from tkinter import *
from tkinter import ttk

#Creating a function  for labels for (Names, reciepts, number hired and the item hired)
def Labels():
    Label(main_window, text="Julies Party Hire", font="bold, 15").grid(column=0, row=0, columnspan = 2, pady = 10)
    Label(main_window, text="Customer name:").grid(column=0, row=1, sticky=E)
    Label(main_window, text="Item Hired:").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Number Hired:").grid(column=0, row=3, sticky=E)
    Label(main_window, text="Reciept # :").grid(column=0, row=4, sticky=E)

#Making entries for the user to input the data
def Entries():
    global Entry_Name, Entry_Number_Hired, Entry_Name, Item

    #Customers name
    Entry_Name = Entry(main_window)
    Entry_Name.grid(column=1, row=1, sticky=W+E)

    #Combobox item list
    Items = ["Catering", "Lighting", "Cutlery", "Party Games", "Decoration" ]
    Item = StringVar()
    Entry_Item_Hired = ttk.Combobox(main_window, value = Items, textvariable = Item, state= 'readonly')
    Entry_Item_Hired.grid(column=1, row=2)

    # Number of items
    Entry_Number_Hired = Entry(main_window)
    Entry_Number_Hired.grid(column=1, row=3, sticky=W+E)

#Creating a function that runs all the other functions
def Main(): 
    global main_window
    main_window=Tk()
    main_window.geometry("600x200")
    Labels()
    Entries()

#calling out the main function
Main()
