import serial, time, re
from tkinter import *

root = Tk()
root.geometry("500x200")
root.resizable(True, True)
root.title("Temperature Reader")
label = Label(master=root)
label.config(font=("Helvetica", 44))

ser = serial.Serial(port='/dev/cu.usbmodem14201')

def read_temperature():
    temp_raw = ser.readline().decode()
    temp = temp_raw.rstrip()
    temp_list = re.split('C|F|:| ', temp)

    temp_cel, temp_fahren = temp_list[3], temp_list[6]

    date_temp = ("{}\n"+"{}"+u"\N{DEGREE SIGN}C"+"\n{}"+u"\N{DEGREE SIGN}F").format(time.strftime('%H:%M:%S'), temp_cel, temp_fahren)
    
    label.configure(text=date_temp)
    root.after(1000, read_temperature)

label.pack()

root.after(1, read_temperature)
root.mainloop()
