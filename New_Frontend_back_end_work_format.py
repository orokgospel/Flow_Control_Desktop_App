import tkinter as tk

import numpy as np


# =========creating main window============

root = tk.Tk()

#for the title of the GUI
root.title("Flow Rate Calculator")

# ====create the main container ================

frame = tk.Frame(root)

# =====layout the main container,to grow with window size, resizing====

frame.pack(fill=tk.BOTH, expand=True)

# ======Allow middle cell of grid to grow when resized  ===

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)


from tkinter import *
#================================================


#adding colour background

root.config(bg="green")

#================Declaring global variables===============
tank_factor = None

batch_size = None

initial_time = None

initial_minute = None

final_time = None

final_minute = None

initial_level = None

final_level = None

initial_volume = None

final_volume = None

change_in_minute = None

minute_in_hr = None

change_in_time = None

change_in_volume = None

total_time = None

flow_rate = None

flow_rate_at_initial_minute =None

flow_rate_at_final_minute = None

minute_flow_rate = None
total = None
value = None
data = None
result = None


#=================function to be called  whenever the button is pressed====
def Run():

    global data
    global tank_factor

    global batch_size

    global initial_time

    global initial_minute

    global final_time

    global final_minute

    global initial_level

    global final_level

    global initial_volume

    global final_volume

    global change_in_minute

    global minute_in_hr

    global change_in_time

    global change_in_volume

    global total_time

    global flow_rate

    global flow_rate_at_initial_minute

    global flow_rate_at_final_minute

    global minute_flow_rate
    global total
    global value
    global data
    global New_volumes

    global Accumulate

    global Net_to_pump
    global result


    f = tank_factor.get()
    b = batch_size.get()
    l = initial_level.get()
    lf = final_level.get()
    t1 = initial_time.get()
    tm1= initial_minute.get()
    t2 = final_time.get()
    tm2 = final_minute.get()


    #to calculate flows and update label through textvariable
    a = float(l * f)

    # final_volume
    af = lf * f

    change_in_minute = tm2 - tm1

    minute_in_hr = change_in_minute / 60

    # change_in_time
    n = int(t2 - t1)

    change_in_volume = a - af
    total_time = n + minute_in_hr

    # flow_rate
    d = int(change_in_volume / total_time)

    New_volumes = []

    Accumulate = []

    Net_to_pump = []

    total = 0
    value = a
    batch = b
    ac = b


    # flow-rate at initial minute
    fim = (tm1 / 60) * d

    # flow_rate_at_final_minute
    ffm = (tm2/ 60) * d

    for i in range(n + 1):
        result.set((i,  value,  d, batch,  ac))
        #print(result)
        New_volumes.append(value)
        batch = batch - d
        total = total + value
        value = value - d
        ac = ac + d

        Accumulate.append(d)

        Net_to_pump.append(d)

    # Levels = np.divide(New_volumes, f)
    Levels = np.divide(New_volumes, f)

    print('\nNew Tank Levels(mm):')

    for l in Levels:
        print(round(l, 3))

    dg = sum(Accumulate) + fim + ffm
    print("\nTotal volume of Product Discharged (ACCUMULATION):", round(dg, 4), 'm3')

    rn = b - dg
    print("\nTotal volume of product remaining(NET To Pump):", round(rn, 4), 'm3')

    bal = dg + rn
    print("Balance Check of Batch Size:", bal)

    # new level at final minute = af-fmm, volume, net to pump, accumulation



tank_factor = tk.DoubleVar()
batch_size = tk.DoubleVar()
initial_time = tk.DoubleVar()
final_time = tk.DoubleVar()
initial_minute = tk.DoubleVar()
final_minute = tk.DoubleVar()
initial_level = tk.DoubleVar()
final_level = tk.DoubleVar()

initial_volume = tk.DoubleVar()
final_volume = tk.DoubleVar()
change_in_minute = tk.DoubleVar()
change_in_time = tk.DoubleVar()
change_in_volume = tk.DoubleVar()
total_time = tk.DoubleVar()
flow_rate = tk.DoubleVar()


flow_rate_at_initial_minute = tk.DoubleVar()
flow_rate_at_final_minute = tk.DoubleVar()
data = tk.DoubleVar()
result = tk.DoubleVar()



#=================================window box parameter title===============

tank_factor_entry= tk.Entry(frame, width=7, textvariable = tank_factor)
label_tf = tk.Label(frame, text="Tank Factor", font=('Arial', 11, 'bold'))

batch_size_entry = tk.Entry(frame, width =7, textvariable = batch_size)
label_bs = tk.Label(frame, text="Batch Size", font=('Arial', 11, 'bold'))


initial_time_entry = tk.Entry(frame, width=7, textvariable = initial_time)
label_it = tk.Label(frame, text="Initial time in hr", font=('Arial', 11, 'bold'))


final_time_entry = tk.Entry(frame, width=7, textvariable = final_time)
label_ft = tk.Label(frame, text="Final time in hr", font=('Arial', 11, 'bold'))


initial_minute_entry = tk.Entry(frame, width=7, textvariable = initial_minute)
label_im = tk.Label(frame, text="Initial Minute", font=('Arial', 11, 'bold'))

final_minute_entry = tk.Entry(frame, width=7, textvariable = final_minute)
label_fm = tk.Label(frame, text="Final Minute", font=('Arial', 11, 'bold'))

initial_level_entry= tk.Entry(frame, width=7, textvariable = initial_level)
label_il = tk.Label(frame, text="Initial Tank Level", font=('Arial', 11, 'bold'))

final_level_entry = tk.Entry(frame, width=7, textvariable = final_level)
label_fl = tk.Label(frame, text="Final Level", font=('Arial', 11, 'bold'))


label_equal = tk.Label(frame, text="RESULT", font=('Arial', 11, 'bold'))

label_result = tk.Label(frame, textvariable = result)

button_run = tk.Button(frame, text="RUN", command = Run)

# =======layout widgets=====
tank_factor_entry.grid(row=0, column=1, padx=5, pady=5)
label_tf.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

batch_size_entry.grid(row=1, column=1, padx=5, pady=5)
label_bs.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

initial_time_entry.grid(row=2, column=1, padx=5, pady=5)
label_it.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

final_time_entry.grid(row=3, column=1, padx=5, pady=5)
label_ft.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

initial_minute_entry.grid(row=4, column=1, padx=5, pady=5)
label_im.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

final_minute_entry.grid(row=5, column=1, padx=5, pady=5)
label_fm.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

initial_level_entry.grid(row=6, column=1, padx=5, pady=5)
label_il.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

final_level_entry.grid(row=7, column=1, padx=5, pady=5)
label_fl.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

label_result.grid(row=9, column=1, padx=5, pady=5)


#label_unitf.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

button_run.grid(row=10, column=0, padx=5, pady=5, sticky=tk.E)


#===========================Window display =========================================
messageWindow=Text(root, bg='white', width=12, height=15,)
messageWindow.place(x=470, y=50, height=445, width=440)
#adding scroll bar
scrollbar=Scrollbar(root, command=messageWindow.yview)
scrollbar.place(x=910, y=50, height=444)

titext=Label(root, text= "NPSC PH-Area PUMP STATION FLOW CONTROL INTERFACE", font=('Arial',11, 'bold'))
titext.place(x=459, y=3, height=23, width=470)

# ====place cursor in entry box by default=======
tank_factor_entry.focus()

# ============run forever
root.mainloop()





