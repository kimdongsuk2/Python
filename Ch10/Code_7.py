from tkinter import *

window = Tk()
window.geometry("300x100")
Label(window, text="ID").place(x=20, y=20)
Label(window, text="PassWord").place(x=20, y=50)

e1 = Entry(window)
e2 = Entry(window)

e1.place(x=80,y=20)
e2.place(x=80,y=50)

window.mainloop()