import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Clock label style
label = tk.Label(root, font=("Helvetica", 80), background="black", foreground="cyan")
label.pack(anchor='center')

# Function to update time
def update_time():
    time_string = strftime('%H:%M:%S %p')  # 24-hour format with AM/PM
    label.config(text=time_string)
    label.after(1000, update_time)  # Update every 1 second

# Start the clock
update_time()
root.mainloop()
