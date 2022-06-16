# importing the tkinter program 
from tkinter import *
from tkinter import ttk
import random


#Creating a function  for labels for (Names, reciepts, number hired and the item hired)
def Labels():
    Label(main_window, text="Julies Party Hire", font="bold, 15").grid(column=0, row=0, columnspan = 2, pady = 10)
    Label(main_window, text="Customer name:").grid(column=0, row=1, sticky=E)
    Label(main_window, text="Item Hired:").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Number Hired:").grid(column=0, row=3, sticky=E)

#Making entries for the user to input the data
def Entries():
    global Entry_Name, reciepts, Entry_Number_Hired, Entry_Name, Item

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
    global Entry_Name, reciepts, Entry_Number_Hired, Entry_Name, reciept
    Button_Append_Details = Button(main_window, text="Update", command=Update).grid(column=2, row=1, padx=10, sticky=W+E)
    Button_Print_Details = Button(main_window, text="Print Details", command=Print_Details).grid(column=2, row=2, padx=10, sticky=W+E)
    Button_Quit = Button(main_window, text="Quit program", command=Quit).grid(column=2, row=3, padx=10, sticky=W+E)    

#This function will store the inputs that the user inputed on the entries into a list which would then be stored in a mutlidimensional list until the user prints it
def Update():
    global Details, Entry_Name, Entry_Item_Hired, Entry_Number_Hired, reciept, Item, Entry_Number, All_reciept
    randomizer()
    Details.append([Entry_Name.get(), Item.get(), Entry_Number_Hired.get(), reciept])
    Entry_Name.delete(0, "end")
    Item.set("")
    Entry_Number_Hired.delete(0, "end")
    Entry_Number+=1

#This function quits the program when the user is done using it
def Quit():
    main_window.destroy()

#This function randomizers a number from 100000 to 1000 for the reciept number 
def randomizer():
    global reciept, All_reciept, Entry_Reciept_Delete
    reciept = "#"+str(random.randint(10000,99999))
    All_reciept.append(reciept)

# This function allows the user to print whatever appended items in the stored multidimensional list. This function also includes combobo for all of the reciepts input
# generated so that the user can delete a specific reciept list, The label for Reciept and the button to initiated the delete reciept command.
def Print_Details():
    global Details, Entry_Name, Entry_Item_Hired, Entry_Number_Hired, reciept, Item, reciept, frame, Name_Count, Entry_Number, All_reciept, Entry_Reciept_Delete
    Name_Count = 0
    Entry_Reciept = ttk.Combobox(main_window, value = All_reciept, textvariable = Item, state= 'readonly')
    Entry_Reciept.grid(column=1, row=4)
    frame.grid(column=3, row=1, columnspan = 4, rowspan = 100, sticky = N)
    Label(frame, text="-=Customer Name=-").grid(column=3, row=0)
    Label(frame, text="-=Item=-").grid(column=4, row=0)
    Label(frame, text="-=Number of the Item=-").grid(column=5, row=0)
    Label(frame, text="-=Reciept=-").grid(column=6, row=0)
    Label(main_window, text="Reciept # :").grid(column=0, row=4, sticky=E)
    Button_Delete_Reciept = Button(main_window, text="Delete Reciept").grid(column=2, row=4, padx=10, sticky=W+E)
    Reciept_List = StringVar()
    Entry_Reciept_Delete = ttk.Combobox(main_window, value = All_reciept, textvariable = Reciept_List, state= 'readonly')
    Entry_Reciept_Delete.grid(column=1, row=4, sticky=W+E)
    while Name_Count < Entry_Number:
        Label(frame, text=(Details[Name_Count][0])).grid(row=1+Name_Count, column=3)
        Label(frame, text=(Details[Name_Count][1])).grid(row=1+Name_Count, column=4)
        Label(frame, text=(Details[Name_Count][2])).grid(row=1+Name_Count, column=5)
        Label(frame, text=(Details[Name_Count][3])).grid(row=1+Name_Count, column=6)
        Name_Count+=1

        

#Creating a function that runs all the other functions
def Main():
    global main_window, Details, frame, Name_Count, Entry_Number, All_reciept, Entry_Reciept_Delete
    Details = []
    All_reciept = []
    Entry_Number = 0
    main_window=Tk()
    main_window.geometry("750x200")
    frame = Frame(main_window)
    Labels()
    Entries()
    Buttons()

#calling out the main function
Main()
