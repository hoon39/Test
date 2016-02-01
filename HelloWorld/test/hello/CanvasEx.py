from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

w.create_rectangle(0, 0, 500, 500, fill="black")

w.create_text(100, 100, text="Test", fill="white", font=("Times new roman",20))

mainloop()