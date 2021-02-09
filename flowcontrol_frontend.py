from tkinter import *
#useful for tk
import tkinter as tk
root=Tk()
root.geometry("900x500")
root.resizable(width=False, height= False)
menu=Frame(root)
#menu=Menu(root)
#for the title of the GUI
root.title("GIPSC.COM")

root.geometry("930x500")
#adding colour background
root.configure(background="light green")

#=================================window box parameter title===============

a = Label(root, text="Time(hr)", bg='green', fg='white',font=('Arial', 9, 'bold'))
a.place(x=470, y=30, height=20, width=54)

a = Label(root, text="Level(mm)", bg='green',fg='white',font=('Arial', 9, 'bold'))
a.place(x=528, y=30, height=20, width=69)


a = Label(root, text="Volume(m3)", bg='green', fg='white',font=('Arial', 9, 'bold'))
a.place(x=600, y=30, height=20, width=78)

a = Label(root, text="FRate(m3/hr)", bg='green',fg='white',font=('Arial', 9, 'bold'))
a.place(x=683, y=30, height=20, width=81)


a = Label(root, text="N2Pump(m3)", bg='green', fg='white',font=('Arial', 9, 'bold'))
a.place(x=768, y=30, height=20, width=81)

a = Label(root, text="Accum.(m3)", bg='green',fg='white',font=('Arial', 9, 'bold'))
a.place(x=853, y=30, height=20, width=74)

#===========================Window display =========================================
messageWindow=Text(root, bg='white', width=12, height=15,)
messageWindow.place(x=470, y=50, height=445, width=440)
#adding scroll bar
scrollbar=Scrollbar(root, command=messageWindow.yview)
scrollbar.place(x=910, y=50, height=444)

titext=Label(root, text= "NPSC PH-Area PUMP STATION FLOW CONTROL INTERFACE", font=('Arial',11, 'bold'))
titext.place(x=459, y=3, height=23, width=470)

#===============================================


#========================Tank Selection===============================
options = ["NONE","52TK57K", "52TK57N", "52TK59G", "59TK59H",]
itemVariable = StringVar()
itemVariable.set(options[0])
quantityVar= StringVar

tank=Label(root, text= "Tank In Use", font=('Arial',11,'bold' ))
tank.place(x=243, y=80, height=23, width=110)
tankDropDown = OptionMenu(root,itemVariable,*options)
tankDropDown.place(x=358, y=78, height=30, width=100)

#=========================Booster Pump=============================
booster = ["NONE","A", "B"]
boostVariable = StringVar()
boostVariable.set(booster[0])
boostVar= StringVar
boost=Label(root, text= "B.P In Use", font=('Arial',11,'bold' ))
boost.place(x=243, y=130, height=23, width=110)
boostDropDown = OptionMenu(root,boostVariable,*booster)
boostDropDown.place(x=358, y=125, height=30, width=100)


#======================Product =========================================
s=Label(root, text= "Product", font=('Arial black',14 ),bg="white",fg="black")
s.place(x=270, y=200, height=23, width=95)

product = ["NONE","PMS", "AGO","H20"]
proVariable = StringVar()
proVariable.set(product[0])
proVar= StringVar
proDropDown = OptionMenu(root,proVariable,*product)
proDropDown.place(x=370, y=190, height=50, width=95)

#=====================FOR BUTTONS ON THE WINDOW==================
s=Label(root, text= "System In Use", font=('Arial black',12 ),bg="white",fg="black")
s.place(x=6, y=200, height=23, width=130)

system = ["NONE","2E", "2EX"]
sysVariable = StringVar()
sysVariable.set(system[0])
sysVar= StringVar
sysDropDown = OptionMenu(root,sysVariable,*system)
sysDropDown.place(x=143, y=190, height=50, width=100)



#===================== EDS=======================================
Button=Button(root, text='RUN', bg='green', activebackground='light blue', width=15, height=5, font=('Arial',20,'bold' ))
Button.place(x=6, y=250, height=50, width=110)

button=tk.Button(root, text='STOP', bg='red',font=('Arial',20,'bold' ))
button.place(x=6, y=320, height=50, width=110 )

#=============================Parameters===================================
#Batch size
a=Label(root, text= "BATCH SIZE", font=('Arial',11,'bold' ))
a.place(x=210, y=3, height=23, width=120,)

messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=333, y=3, height=23, width=100)


#Initial level
a=Label(root, text= "Initial Level(mm)", font=('Arial',11,'bold' ))
a.place(x=6, y=80, height=23, width=120)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=140, y=80, height=23, width=100)

#Final level
a=Label(root, text= "Final Level(mm)", font=('Arial',11,'bold' ))
a.place(x=6, y=130, height=23, width=120)
messageWindow=Text(root, bg='white', width=50, height=4,)
messageWindow.place(x=140, y=130, height=23, width=100)

#Tank Factor
a=Label(root, text= "Tank Factor", font=('Arial',11 ,'bold'))
a.place(x=6, y=3, height=23, width=120)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=135, y=4, height=23, width=70)


#Initial time block
a=Label(root, text= "Initial Time(hrs)", font=('Arial',11,'bold' ))
a.place(x=6, y=30, height=23, width=120)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=135, y=30, height=23, width=40)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=165, y=30, height=23, width=40)

#Final time block
a=Label(root, text= "Final Time(hrs)", font=('Arial',11,'bold' ))
a.place(x=210, y=30, height=23, width=118)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=333, y=30, height=23, width=50)
messageWindow=Text(root, bg='white', width=30, height=4,)
messageWindow.place(x=380, y=30, height=23, width=50)

#======================== PICTURE AND BRAND NAME===================

s=Label(root, text= "©GIPSC.com \n", font=('Arial black',25 ),bg="light green",fg="black")
s.place(x=6, y=420, height=67, width=275)

from PIL import ImageTk, Image
img = Image.open("gipsc.jpg")
img = img.resize((100, 90))

my = ImageTk.PhotoImage(img)

label = Label(root, image = my)
label.place(x = 260, y= 370)


root.mainloop()
