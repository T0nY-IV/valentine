import tkinter as tk
from tkinter import ttk, messagebox
import time
import winsound
def decimal_to_bcd(decimal_num):
    upper_digit = decimal_num // 10
    lower_digit = decimal_num % 10
    return upper_digit, lower_digit

def update_clock():
    global alarm_time

    current_time = time.strftime("%H%M%S")
    hours = int(current_time[0:2])
    minutes = int(current_time[2:4])
    seconds = int(current_time[4:6])

    h1, h2 = decimal_to_bcd(hours)
    m1, m2 = decimal_to_bcd(minutes)
    s1, s2 = decimal_to_bcd(seconds)

    label_h1.config(text=str(h1))
    label_h2.config(text=str(h2))
    label_m1.config(text=str(m1))
    label_m2.config(text=str(m2))
    label_s1.config(text=str(s1))
    label_s2.config(text=str(s2))

    if alarm_time and current_time == alarm_time.replace(":", ""):
        trigger_alarm()

    root.after(1000, update_clock)

def trigger_alarm():
    messagebox.showinfo("⏰ Alarm", "Time's up!")
    try:
        winsound.Beep(1000, 1000)
    except:
        pass  

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get().strip()
    
    if len(alarm_time) == 8 and alarm_time[2] == ':' and alarm_time[5] == ':':
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid time (HH:MM:SS).")
        alarm_time = None


root = tk.Tk()
root.title("Clock")
root.geometry("500x400")

frame = ttk.LabelFrame(root, text="", padding=50) 
frame.pack(pady=20) 

font_style = ("Seven Segment", 36)

label_h1 = ttk.Label(frame, text="0", font=font_style)
label_h1.grid(row=0, column=0, padx=5)
label_h2 = ttk.Label(frame, text="0", font=font_style)
label_h2.grid(row=0, column=1, padx=5)
ttk.Label(frame, text=":", font=font_style).grid(row=0, column=2, padx=5)
label_m1 = ttk.Label(frame, text="0", font=font_style)
label_m1.grid(row=0, column=3, padx=5)
label_m2 = ttk.Label(frame, text="0", font=font_style)
label_m2.grid(row=0, column=4, padx=5)
ttk.Label(frame, text=":", font=font_style).grid(row=0, column=5, padx=5)
label_s1 = ttk.Label(frame, text="0", font=font_style)
label_s1.grid(row=0, column=6, padx=5)
label_s2 = ttk.Label(frame, text="0", font=font_style)
label_s2.grid(row=0, column=7, padx=5)

alarm_frame = ttk.LabelFrame(root, text=" Set Alarm ", padding=10)
alarm_frame.pack(pady=10)

ttk.Label(alarm_frame, text="Enter Time (HH:MM:SS):").pack(side="left", padx=5)
alarm_entry = ttk.Entry(alarm_frame, width=15)
alarm_entry.pack(side="left", padx=5)
ttk.Button(alarm_frame, text="Set Alarm", command=set_alarm).pack(side="left", padx=5)

alarm_time = None

update_clock()

root.mainloop()
