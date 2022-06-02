from tkinter import  *
window = Tk()

window.title("윈도우 창 연습")

photo =PhotoImage(file="img/Drone.png")
label1 = Label(window, image=photo)

photo2 =PhotoImage(file="img/Drone1.png")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
# label1.pacr(side=RIGHT)
label2.pack()

window.mainloop()
