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


#Creating buttons for the user to click and produce a result
def Buttons():
    global Entry_Name, reciepts, Entry_Number_Hired, Entry_Name
    Button_Append_Details = Button(main_window, text="Update", command=Update).grid(column=2, row=1, padx=10, sticky=W+E)
    Button_Print_Details = Button(main_window, text="Print Details", command=Print).grid(column=2, row=2, padx=10, sticky=W+E)
    Button_Append_Details = Button(main_window, text="Quit program", command=Quit).grid(column=2, row=3, padx=10, sticky=W+E)
    Button_Append_Details = Button(main_window, text="Delete Reciept", command=Delete).grid(column=2, row=4, padx=10, sticky=W+E)

#Creating a function that runs all the other functions
def Main():
    global main_window
    Details = []
    main_window=Tk()
    main_window.geometry("600x200")
    Labels()
    Entries()
    Buttons()

#calling out the main function
Main()
