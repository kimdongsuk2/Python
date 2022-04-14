import  turtle as t

h=int(input("Enter the height of the Rectangle: "))
w=int(input("Enter the height of the Rectangle: "))

for i range(4):

    #drawing height
    if i%2==0:
        t.forward(h) # Forward turtle by l units
        t.left(90) # turn turtle by 90 begree

     #drawing width
    else:
        t.forward(w) #Forward turtle by w units
        t.left(90) #Turn turtle by 90 degree

    t.done()
