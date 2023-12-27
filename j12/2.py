import sqlite3
from tkinter import *
from tkinter import messagebox

# connect to the sqlite database or create it if it doesn't exist
conn = sqlite3.connect('notes.db')
c = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY, content TEXT)
'''

# create the notes table if it doesn't exist
c.execute(sql)

# function to insert a note into the database
def insert_note():
    content = e.get()
    if content:
        c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        e.delete(0, END)
        messagebox.showinfo('Success', 'Note added successfully')
    else:
        messagebox.showerror('Error', 'Note content is required')

# function to retrieve all notes from the database
def retrieve_notes():
    notes = c.execute("SELECT content FROM notes")
    output = '\n'.join([note[0] for note in notes])
    t.delete(1.0, END)
    t.insert(END, output)

root = Tk()
root.title('Note App')

mainframe = Frame(root)
mainframe.pack(padx=10, pady=10)

e = Entry(mainframe, width=100)
e.pack(padx=5, pady=5)

b1 = Button(mainframe, text='Add Note', command=insert_note)
b1.pack(padx=5, pady=5)

b2 = Button(mainframe, text='View Notes', command=retrieve_notes)
b2.pack(padx=5, pady=5)

t = Text(root, wrap=WORD)
t.pack(padx=10, pady=10)

root.mainloop()
conn.close()