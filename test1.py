from tkinter import *

def printHello():
    print('HI!')

root = Tk()

w = Label(root, text='Python Test')
b = Button(root, text="Hello Python", command=printHello)
c = Button(root, text='Quit', comman=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()