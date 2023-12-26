import tkinter as tk

def show_full_name():
    full_name = f"{entry_first_name.get()} {entry_last_name.get()}"
    label_full_name.config(text="full name: " + full_name)

# Create the main window
app = tk.Tk()
app.title("Name App")

# Create and place Entry widgets for first name and last name

label_first_name = tk.Label(app, text="first name: ")
label_first_name.grid(row=0, column=0, padx=10, pady=10)

label_last_name = tk.Label(app, text="last name: ")
label_last_name.grid(row=1, column=0, padx=10, pady=10)

entry_first_name = tk.Entry(app, width=20)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

entry_last_name = tk.Entry(app, width=20)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

# Create and place Submit button
submit_button = tk.Button(app, text="Submit", command=show_full_name)
submit_button.grid(row=2, column=0, pady=10)

# Create and place Label to display full name
label_full_name = tk.Label(app, text="hi")
label_full_name.grid(row=3, column=0, pady=10)

# Start the Tkinter event loop
app.mainloop()

