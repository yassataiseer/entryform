import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import Listbox

screen=tkinter.Tk()
screen.geometry('1000x500')
screen.title('Entry form')
frame=Frame(screen)
frame.grid(row=0,column=0)

var = IntVar()



l3=tkinter.Label(frame,text="Student Name",font=("Fixed",14),fg="Black")
l3.grid(row=2,column=0)

e2=tkinter.Entry(frame,width=25)
e2.grid(row=2,column=1)


l3=tkinter.Label(frame,text="Gender",font=("Fixed",14),fg="red")
l3.grid(row=3,column=0)

gender = tkinter.Radiobutton(frame,text="Male",font=("Fixed",14),fg="Blue",variable=var,value=1)
gender.grid(row=3,column=1)

gender = tkinter.Radiobutton(frame,text="female",font=("Fixed",14),fg="Pink",variable=var,value=2)
gender.grid(row=3,column=2)


listbox_entries = ["Grade 1", "Grade 2",
                   "Grade 3", "Grade 4","Grade 5","Grade 6","Grade 7","Grade 8"]
listbox_widget = tkinter.Listbox(frame)
for entry in listbox_entries:
    listbox_widget.insert(tkinter.END, entry)
l6=tkinter.Label(frame,text="Grade",font=("Fixed",14),fg="Blue")
l6.grid(row=4,column=1)
listbox_widget.grid(row=5,column=1)


l7=tkinter.Label(frame,text="Address",font=("Fixed",14),fg="Black")
l7.grid(row=6,column=0)

e7=tkinter.Entry(frame,width=25)
e7.grid(row=6,column=1)
###Buttons####



def ext():
    screen.destroy()
def save():
    a=var.get()
    print (a)
    gender = ""
    if a ==1:
        gender = "Male"
    else:
        gender = "Female"
    print(gender)
    file_name= "\nStudent Name: "+e2.get()+"|Gender: "+ gender+"|Grade: "+listbox_widget.get(listbox_widget.curselection())+"|Adress:"+ e7.get()
    print(file_name)
    with  open("entries.txt","w")as f:
        f.write(file_name)
        f.close()
l1=tkinter.Label(frame,text="Entry Form",font=("Fixed",18),fg="blue")
l1.grid(row=0,column=1)

save = tkinter.Button(frame,text = "save" ,command=save)
save.grid(row=7,column=1)

exiter = tkinter.Button(frame,text = "exit" ,command=ext)
exiter.grid(row=7,column=2)

screen.mainloop()
