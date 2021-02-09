#Make sure you have numpy library module installed if not using jupyter note
import numpy as np


#=============================================

def run():
    tank = input("Enter Tank Name:")

    #tank_factor
    f = eval(input("Enter the Tank factor:"))

    #Batch_size
    b = eval(input("Enter the Batch size to pump: "))

    initial_time = int(input("Enter the Initial Time in hour: "))
    initial_minute = float(input("Enter the initial Minute time: "))
    final_time = int(input("Enter the Final time in hour: "))
    final_minute = float(input("Enter the Final Minute time: "))

    #initial_level
    l = eval(input("Enter the initial tank level: "))

    #final_level
    lf = eval(input("Enter the final Tank level: "))

    #Initial volume
    a = float(l * f)

    #final_volume
    af = lf * f

    change_in_minute = final_minute - initial_minute

    minute_in_hr = change_in_minute / 60

    #change_in_time
    n = final_time - initial_time

    change_in_volume = a - af
    total_time = n + minute_in_hr

    #flow_rate fomula
    d = change_in_volume / total_time

    New_volumes = []

    Accumulate = []

    Net_to_pump = []

    total = 0
    value = a
    batch = b
    ac = 0

    print("\n*************************Flow Result for",tank,"**********************")
    
    print("Start-up Time", initial_time, int(initial_minute), sep=":")

    print("Shut-down Time", final_time, int(final_minute), sep=":")

    print("\nGeneral Flow-Rate Value is", round(d, 4), 'm3/hr', "~~", round(d), 'm3/hr')

    #flow-rate at initial minute
    fim = (initial_minute / 60) * d

    #flow_rate_at_final_minute
    ffm = (final_minute / 60) * d

    print("Flow-Rate at Initial Minute of", int(initial_minute),'minute''=', round(fim, 3),
          'm3/min')

    print("Flow-Rate at Final Minute of", int(final_minute),'minute of', final_time,':',int(final_minute),'=', round(ffm, 4), 'm3/hr',
          "~~", round(ffm), 'm3/hr')

    print("\nTime(hr), Volume(m3), Flow-rate(m3/hr),             Net-to-Pump(m3),     Accumulation(m3)")

    for i in range(n+1):
        print( i,"       ","%d " %value,"    ", d, "             ","%d" %batch,"            ", "%d" %ac, )
        New_volumes.append(value)
        batch = batch - d
        total = total + value
        value = value - d
        ac = ac + d

        Accumulate.append(d)

        Net_to_pump.append(d)

    Levels = np.divide(New_volumes, f)

    print('\nNew Tank Levels(mm):')

    for l in Levels:
        print( round(l,3))

    dg = sum(Accumulate)+ fim + ffm
    print("\nTotal volume of Product Discharged (ACCUMULATION):", round(dg, 4), 'm3')

    rn = b - dg
    print("\nTotal volume of product remaining(NET To Pump):", round(rn, 4), 'm3')

    bal= dg + rn
    print("Balance Check of Batch Size:", bal)

    #new level at final minute = af-fmm, volume, net to pump, accumulation

run()

