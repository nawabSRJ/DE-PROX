# *this is the final code for the DE-PROX Presentation
import tkinter as tk
from tkinter import * 
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
current_window = None  # To store the current open window
# *-------------------------------- DE-PROX stuPart ------------------------------------------
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
        uid = int(id_entry.get())
        if uid == 0:
            return
        if uid < 1 or uid > 10:
            # print("\n\t\tALERT!!!\nInvalid Id...you have to enter again!!!\n")
            ttk.Label(root, text = "Invalid ID Entered").grid(column = 1, row = 3, sticky = W)

        else:
            match(uid)
            absent()
    except ValueError:
        print("\n\t\tALERT!!!\nInvalid input...you have to enter a valid id!!!\n")

def Put_Atn():
    with open("Test_1.xls", "w") as fp:
            fp.write("ID\t    Name\t    Attendance\n")
            for student in students:
                fp.write(f"{student.id}    \t    {student.name}  \t     {student.attendance}\n")
                print("\n\n<-----DATA ENTERED----->\n\n")
                print("\n\t\tThank You for Marking Attendance with DE-PROX\n\n")
                
def clear_entry(event):
    mark_attendance()
    id_entry.delete(0, 'end')  # * Clear the entry widget
# *-----------------------------------------------------------------------------


def show_window(window_name):
    global current_window
    
    if current_window:  # Check if a window is open
        current_window.destroy()  # Close the open window
        
    text = {
        "second": "Second Window",
        "third": "Third Window"
    }
    
    current_window = tk.Toplevel(root)
    current_window.geometry("800x800")
    current_window.configure(bg="#040D12")
    
    label = tk.Label(current_window, text=text[window_name], font=("Helvetica", 20), fg="white", bg="#040D12")
    label.pack(pady=20)
    
root = tk.Tk()
root.geometry("1000x800")
root.configure(bg="#040D12")
root.title("App")


side_panel = tk.Frame(root, bg="#F7E987")
side_panel.place(x=0, y=0, relheight=1, width=220)

button_style = {"font": ("Helvetica", 16), "fg": "black", "bg": "#F7E987", "relief": "flat", "borderwidth": 0}

button1 = ttk.Button(side_panel, text="First Option", style="Rounded.TButton")
button1.pack(fill=tk.X, pady=(20, 10), padx=10)

button2 = ttk.Button(side_panel, text="Second Option", command=lambda: show_window("second"), style="Rounded.TButton")
button2.pack(fill=tk.X, pady=15, padx=10)

button3 = ttk.Button(side_panel, text="Third Option", command=lambda: show_window("third"), style="Rounded.TButton")
button3.pack(fill=tk.X, pady=10, padx=10)

style = ttk.Style()
style.configure("Rounded.TButton", background="black")


# *----------- DE-PROX GUI Part ----------
stu = StringVar()

text_label = tk.Label(root, text="Mark Your Attendance", font=("Helvetica", 25), fg="white", bg="#040D12")
text_label.place(x="735", y="80", anchor="center")  

id_entry =  customtkinter.CTkEntry(root, width=150)
id_entry.pack(pady=20)
id_entry.place(x = 720,y = 150 , anchor="center")

# Bind the Enter key to the clear_entry function
id_entry.bind("<Return>", clear_entry)

# * Mark Button
b = customtkinter.CTkButton(root , text = 'Mark' , command=mark_attendance)
b.place(x =580 , y = 220)

# * Put Attendance Button
b = customtkinter.CTkButton(root , text = 'Done' , command=Put_Atn)
b.place(x =760 , y = 220)



root.mainloop()
