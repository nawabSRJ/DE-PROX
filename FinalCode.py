# *this is the final code for the DE-PROX Presentation
from tkinter import *   # * (*) imports all the functions of the Module at once
from tkinter import ttk
import customtkinter

# *-------------------------------- DE-PROX Part ------------------------------------------
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.attendance = 'A'

students = [
    Student(1, "Anshika Nagbanshi"),
    Student(2, "Aisha Sidiqui"),
    Student(3, "Mahima Manni"),
    Student(4, "Maalav Whorra"),
    Student(5, "Saad Malick"),
    Student(6, "Sparsh Shukla"),
    Student(7, "Sumati Gaur"),
    Student(8, "Pratham Gupta"),
    Student(9, "Pari Gupta"),
    Student(10, "Aakansha Patel")
]

def match(n):
    for student in students:
        if n == student.id:
            student.attendance = 'P'

def absent():
    for student in students:
        if student.attendance != 'P':
            student.attendance = 'A'
def mark_attendance():
    try:
        uid = int(feet.get())
        if uid == 0:
            return
        if uid < 1 or uid > 10:
            # print("\n\t\tALERT!!!\nInvalid Id...you have to enter again!!!\n")
            ttk.Label(mainframe, text = "Invalid ID Entered").grid(column = 1, row = 3, sticky = W)

        else:
            match(uid)
            absent()
    except ValueError:
        print("\n\t\tALERT!!!\nInvalid input...you have to enter a valid id!!!\n")

def Put_Atn():
    with open("test1.xls", "w") as fp:
            fp.write("ID\t    Name\t    Attendance\n")
            for student in students:
                fp.write(f"{student.id}    \t    {student.name}  \t     {student.attendance}\n")
                print("\n\n<-----DATA ENTERED----->\n\n")
                print("\n\t\tThank You for Marking Attendance with DE-PROX\n\n")

# *-------------------------------- GUI Part ------------------------------------------
root = Tk()
root.title("DE-PROX")
# root.geometry("720x480")

root.minsize(400, 300)  # Minimum width of 400 and minimum height of 300
root.maxsize(800, 600)  # Maximum width of 800 and maximum height of 600



# * we create a frame widget, which will hold the contents of our user interface.
mainframe = ttk.Frame(root , padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0 , sticky = (N, W, E, S))

root.columnconfigure(0 , weight = 1)
root.rowconfigure(0 , weight = 1)
# title = customtkinter.CTkLabel(mainframe, text = 'MARK YOUR ATTENDANCE')
# title.grid(column = 1, row = 1)
title_font = ("Helvetica", 30)  # You can adjust the font family and size here
title = customtkinter.CTkLabel(mainframe, text='MARK YOUR ATTENDANCE', font=title_font)
title.grid(column=17, row=0, columnspan=2)  # Place it at the top of the grid

feet = StringVar()
id_entry = ttk.Entry(mainframe , width = 7, textvariable=feet) 

id_entry.grid(column = 17 , row = 3,sticky = (N, W, E, S))

ttk.Label(mainframe, text = "Enter Your ID Here : ").grid(column = 16, row = 3, sticky = W)
# * Mark Button

b = customtkinter.CTkButton(mainframe , text = 'Mark' , command=mark_attendance)
b.grid(column=17, row=4, sticky=(W, E))

# * Put Attendance Button

b = customtkinter.CTkButton(mainframe , text = 'Done' , command=Put_Atn)
b.grid(column=18, row=4, sticky=(W, E))



# * Adding Space between Elements
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
id_entry.focus()
root.bind("<Return>", match)
# * Run the App
root.mainloop()