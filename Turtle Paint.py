from tkinter import *
import turtle
t = turtle.Pen()

def reset():
    t.reset()

def cubered():
    t.color(1, 0, 0)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.end_fill()

def cubeblue():
    t.color(0, 0, 1)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.end_fill()

def cubegreen():
    t.color(0, 1, 0)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.end_fill()

def cube():
    root = Tk()
    root.geometry('250x50')
    root.title('Select your colour')
    b1=Button(root, text='Red', command=cubered)
    b1.place(x = 10, y = 10)
    b2=Button(root, text='Green', command=cubegreen)
    b2.place(x = 50, y = 10)
    b3=Button(root, text='Blue', command=cubeblue)
    b3.place(x = 100, y = 10)
    b4=Button(root, text='Reset', command=reset)
    b4.place(x = 140, y = 10)
    root.mainloop()
    

def circlered():
    t.color(1, 0, 0)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def circlegreen():
    t.color(0, 1, 0)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def circleblue():
    t.color(0, 0, 1)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def dmod():
    root.config(bg='gray22')

def light():
    root.config(bg='white')

def triangleblue():
    for x in range(1, 20):
        t.forward(100)
        t.left(95)
    

def circle():
    root = Tk()
    root.geometry('250x50')
    root.title('Select your colour')
    b1=Button(root, text='Red', command=circlered)
    b1.place(x = 10, y = 10)
    b2=Button(root, text='Green', command=circlegreen)
    b2.place(x = 50, y = 10)
    b3=Button(root, text='blue', command=circleblue)
    b3.place(x = 100, y = 10)
    b4=Button(root, text='Reset', command=reset)
    b4.place(x = 140, y = 10)
    root.mainloop()

root = Tk()
root.geometry('650x50')
root.title('Select Figure')
b11=Button(root, text='Dark', command=dmod)
b11.place(x = 605, y = 10)
b11=Button(root, text='Light', command=light)
b11.place(x = 550, y = 10)
b0=Button(root, text='Cube', command=cube)
b0.place(x = 10, y = 10)
b9=Button(root, text='Circle', command=circle)
b9.place(x = 60, y = 10)
b8=Button(root, text='Star', command=triangleblue)
b8.place(x = 110, y = 10)

root.mainloop()







            















    

    

