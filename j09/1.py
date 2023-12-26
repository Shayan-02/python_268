import tkinter as tk


def lbl_full():
    full_name = f"{entry_first_name.get()} {entry_last_name.get()}"
    lbl_full.config(text="full name: " + full_name)

window = tk.Tk()
window.title("full name")
window.resizable(0, 0)
window.geometry("350x350")

lbl_first_name = tk.Label(window, text="first name", font=("arial", 15)).grid(row=0, column=0, pady=5)
lbl_last_name = tk.Label(window, text="last name", font=("arial", 15)).grid(row=1, column=0, pady=5)
btn_submit = tk.Button(window, text="submit", font=("arial", 15), bg="lightgreen", command= lbl_full).grid(row=2, column=1)
entry_first_name = tk.Entry(window, width=20).grid(row=0, column=1, pady=10, padx=5)
entry_last_name = tk.Entry(window, width=20).grid(row=1, column=1, pady=10, padx=5)
lbl_full_name = tk.Label(window, text="").grid(row=3, column=1)
window.mainloop()

