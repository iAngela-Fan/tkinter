from tkinter import *
from PIL import Image, ImageTk

tk=Tk()
p1=Image.open('/Users/iAngela/Desktop/自主學習/tkinter/p1.png')
gra=ImageTk.PhotoImage(p1)
lbll=Label(tk,image=gra)
lbll.pack()
tk=mainloop()
