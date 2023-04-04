import tkinter as tk

# Define the function to calculate the total hours
def calculate_hours():
    # Get the time in and time out for each day
    monday_in = float(monday_in_entry.get())
    monday_out = float(monday_out_entry.get())
    tuesday_in = float(tuesday_in_entry.get())
    tuesday_out = float(tuesday_out_entry.get())
    wednesday_in = float(wednesday_in_entry.get())
    wednesday_out = float(wednesday_out_entry.get())
    thursday_in = float(thursday_in_entry.get())
    thursday_out = float(thursday_out_entry.get())
    friday_in = float(friday_in_entry.get())
    friday_out = float(friday_out_entry.get())

    # Calculate the total hours worked for the week
    total_hours = monday_out - monday_in + tuesday_out - tuesday_in + wednesday_out - wednesday_in + thursday_out - thursday_in + friday_out - friday_in

    # Update the total hours label
    total_hours_label.config(text="Total Hours: {:.2f}".format(total_hours))

# Create the main window
window = tk.Tk()
window.title("Biweekly Time Sheet")

# Create the labels and entries for each day
monday_label = tk.Label(window, text="Monday:")
monday_in_label = tk.Label(window, text="Time In:")
monday_out_label = tk.Label(window, text="Time Out:")
monday_in_entry = tk.Entry(window)
monday_out_entry = tk.Entry(window)

tuesday_label = tk.Label(window, text="Tuesday:")
tuesday_in_label = tk.Label(window, text="Time In:")
tuesday_out_label = tk.Label(window, text="Time Out:")
tuesday_in_entry = tk.Entry(window)
tuesday_out_entry = tk.Entry(window)

wednesday_label = tk.Label(window, text="Wednesday:")
wednesday_in_label = tk.Label(window, text="Time In:")
wednesday_out_label = tk.Label(window, text="Time Out:")
wednesday_in_entry = tk.Entry(window)
wednesday_out_entry = tk.Entry(window)

thursday_label = tk.Label(window, text="Thursday:")
thursday_in_label = tk.Label(window, text="Time In:")
thursday_out_label = tk.Label(window, text="Time Out:")
thursday_in_entry = tk.Entry(window)
thursday_out_entry = tk.Entry(window)

friday_label = tk.Label(window, text="Friday:")
friday_in_label = tk.Label(window, text="Time In:")
friday_out_label = tk.Label(window, text="Time Out:")
friday_in_entry = tk.Entry(window)
friday_out_entry = tk.Entry(window)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_hours)

# Create the total hours label
total_hours_label = tk.Label(window, text="Total Hours: ")

# Grid the labels and entries on the window
monday_label = tk.Label(window , text = "Monday")
monday_label.grid(row=0, column=0)
monday_In_label = tk.Label(window, text="In:")
monday_in_label.grid(row=1, column=0)
monday_out_label = tk.Label(window), text="Out:")
monday_out_label.grid(row=2, column=0)
monday_in_entry.grid(row=1, column=1)
monday_out_entry.grid(row=2, column=1)

tuesday_label.grid(row=3, column=0)
tuesday_in_label.grid(row=4, column=0)
tuesday_out_label.grid(row=5, column=0)
tuesday_in_entry.grid(row=4, column=1)
tuesday_out_entry.grid(row=5, column=1)

# Wednesday
wednesday_label = tk.Label(window, text="Wednesday")
wednesday_label.grid(row=6, column=0)
wednesday_in_label = tk.Label(window, text="In:")
wednesday_in_label.grid(row=6, column=2)
wednesday_out_label = tk.Label(window, text="Out:")
wednesday_out_label.grid(row=6, column=4)
wednesday_in_entry = Entry(root)
wednesday_in_entry.grid(row=6, column=3)
wednesday_out_entry = Entry(root)
wednesday_out_entry.grid(row=6, column=5)

# Thursday
thursday_label = tk.Label(window, text="Thursday")
thursday_label.grid(row=7, column=0)
thursday_in_label = tk.Label(window, text="In:")
thursday_in_label.grid(row=7, column=2)
thursday_out_label = tk.Label(window, text="Out:")
thursday_out_label.grid(row=7, column=4)
thursday_in_entry = Entry(root)
thursday_in_entry.grid(row=7, column=3)
thursday_out_entry = Entry(root)
thursday_out_entry.grid(row=7, column=5)

# Friday
friday_label = tk.Label(window, text="Friday")
friday_label.grid(row=8, column=0)
friday_in_label = tk.Label(window, text="In:")
friday_in_label.grid(row=8, column=2)
friday_out_label = tk.Label(window, text="Out:")
friday_out_label.grid(row=8, column=4)
friday_in_entry = Entry(root)
friday_in_entry.grid(row=8, column=3)
friday_out_entry = Entry(root)
friday_out_entry.grid(row=8, column=5)

root.mainloop()
