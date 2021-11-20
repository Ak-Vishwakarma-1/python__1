from tkinter import*
from tkinter import font
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
root = Tk()

root.geometry("800x700")
root.title("registration pannel")
root.configure(bg="silver")

img  = Image.open("register.png") 
img = img.resize((355,200))
my = ImageTk.PhotoImage(img)

lbl = Label(image = my)     
lbl = Label(root,image = my)
lbl.place(x=200,y=50)                                               

def action():
    name = e1.get()
    reg_no  = e2.get()
    gen = gender.get()

    room = listroom.get()
    course1=""
    course2=""
    course3=""
    if(var1.get()== "1"):
        course1="java"     
    if(var2.get()== "1"):
        course2="Python"
    if(var3.get()== "1"):
        course3="cpp"
    course4 = course1+" "+course2+" "+course3
    conn = sqlite3.connect("company.db") 
    c=conn.cursor()
    # c.execute("DROP TABLE person")
    # c.execute("CREATE TABLE person(name TEXT, age TEXT ,gen Text, room TEXT ,course TEXT)")
    c.execute("INSERT INTO person VALUES('"+name+"','"+reg_no+"','"+gen+"','"+room+"','"+course4+"')")
    messagebox.showinfo("Information","Your record is inserted !!")
    conn.commit()
    conn.close()

def nexte():
    nx = Tk()
    nx.geometry("700x700")
    nx.configure(bg="silver")
    # nx.maxsize(500,650)
    # nx.minsize(500,650)
    nx.title("Student registration report")
    
    lb1=Label(nx,text="Student registraion records",font="tiem 15 bold",bg="blue",fg="white",padx=120,pady=10)
    lb1.grid(row=0,column=0,columnspan=50)
    lb1.place()
    
    lb2=Label(nx,text="Name",font="time 15 bold")
    lb2.grid(row=1,column=0,padx=10,pady=10)
    
    lb3=Label(nx,text="Reg_no",font="time 15 bold")
    lb3.grid(row=1,column=1,padx=10,pady=10)
    
    lb4=Label(nx,text="Gender",font="time 15 bold")
    lb4.grid(row=1,column=2,padx=10,pady=10)
    
    lb5=Label(nx,text="Room",font="time 15 bold")
    lb5.grid(row=1,column=3,padx=10,pady=10)
    
    lb6=Label(nx,text="Course",font="time 15 bold")
    lb6.grid(row=1,column=4,padx=10,pady=10)

    conn = sqlite3.connect("company.db")
    c = conn.cursor()
    c.execute("SELECT * FROM person")
    r = c.fetchall()
    
    num = 2
    for i in r :
        name  = Label(nx,text = i[0],font="time 12 bold",fg="blue")
        name.grid(row=num,column=0,padx=10,pady=10)
        
        Reg_n= Label(nx,text = i[1],font="time 12 bold",fg="blue")
        Reg_n.grid(row=num,column=1,padx=10,pady=10)
        
        gender= Label(nx,text = i[2],font="time 12 bold",fg="blue")
        gender.grid(row=num,column=2,padx=10,pady=10)
        
        room  = Label(nx,text = i[3],font="time 12 bold",fg="blue")
        room.grid(row=num,column=3,padx=10,pady=10)
        
        course  = Label(nx,text = i[4],font="time 12 bold",fg="blue")
        course.grid(row=num,column=4,padx=10,pady=10)
        
        num = num + 1
    conn.commit()
    conn.close()
 
l1=Label(root,text="Student Registration Panel",font="time 20 bold",background="yellow")
l1.place(x=200,y=0)

l2 = Label(root,text="Enter Name",font = "time 15 bold",bg="light green")
l2.place(x=30,y=300) 

e1 = Entry(root,width=30,bd=5,bg="grey")
e1.place(x=400,y=300)

l3 = Label(root,text="Enter reg no",font= "time 15 bold",bg="light green")
l3.place(x=30,y=350)

e2 = Entry(root,width=30,bd=5,bg="grey")
e2.place(x=400,y=350)

l4=Label(root,text="Select your gender",font="time 15 bold",bg="light green")
l4.place(x=30,y=400)

gender=StringVar()
g1 = Radiobutton(root,text="male",variable=gender,value="male",font="tiem.15",bg="light blue")
g1.place(x=400,y=400)
g1.select()

g2 = Radiobutton(root,text="female",variable=gender,value="female",font="tiem 15",bg="light blue")
g2.place(x=500,y=400)
g2.deselect()

l5 = Label(root,text="Select room",font= "time 15 bold",bg="light green")
l5.place(x=30,y=450)

lists = ["Ac Room","Non AC Room"]
listroom = StringVar(root)
listroom.set("Select Your Room Type")
Menu = OptionMenu(root,listroom,*lists) 
Menu.place(x=400,y=450)

l6=Label(root,text="Select course",font="time 15 bold",bg="light green")
l6.place(x=30,y=500)

var1=StringVar()
l7 = Checkbutton(root,text="java",variable=var1,font="time.15",bg="light blue")
l7.place(x=400,y=500)
l7.deselect()

var2=StringVar()
l8 = Checkbutton(root,text="python",variable=var2,font=" time 15",bg="light blue")
l8.place(x=500,y=500)
l8.deselect()

var3=StringVar()
l7 = Checkbutton(root,text="cpp",variable=var3,font="time.15",bg="light blue")
l7.place(x=630,y=500)
l7.deselect()


button1  = Button(root,text="Submit",fg="white",bg="blue",font = "time 15 bold",width=50,command=action) # fg=foreground when you click on the button 
button1.place(x=30,y=550)                                                        # then it will show the colour

button2= Button(root,text="Exit",foreground="White",background="red",font="time 15 bold",width=23,
command=root.quit) #if you put paranthesis after quit() like this then it will not work
button2.place(x=350,y=600)

button3=Button(root,text="Show",fg="black",bg="sky blue",font="time 15 bold",width=23,command=nexte)
button3.place(x=30,y=600)
root.mainloop()
