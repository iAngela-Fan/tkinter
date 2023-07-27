from tkinter import *
from PIL import Image, ImageTk

tk=Tk()
gra=PhotoImage(file='download.png')  #不能用修改後綴的方式
lbll=Label(tk,image=gra)
lbll.pack()
tk=mainloop()
