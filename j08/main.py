from tkinter import *

window = Tk()
window.title("first app")
window.geometry("500x500")
window.resizable(False, True)
window.config(bg = "lightblue")

l1 = Label(window, text="firstname: ", bg = "lightblue", fg = "black", font=("Arial", 20)).place(x = 5, y = 5)
e1 = Entry(window, width=30).place(x = 150, y = 15)
l2 = Label(window, text="lastname: ", bg = "lightblue", fg = "black", font=("Arial", 20)).place(x = 5, y = 45)
e2 = Entry(window, width=30).place(x = 150, y = 55)
b1 = Button(window, text="submit", bg = "lightblue", fg = "black", width=15, font=("Arial", 20)).place(x = 100, y = 95)
window.mainloop()