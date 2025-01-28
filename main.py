import tkinter as tk
from tkinter import messagebox
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    messagebox.showinfo("Ransomware Simulation", "Time is up! Your files are encrypted!")

def start_simulation():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    countdown(10)  # Set countdown for 10 seconds
    root.mainloop()

if __name__ == "__main__":
    start_simulation()
