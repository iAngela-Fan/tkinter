from tkinter import *
tk=Tk()
gra=PhotoImage(file='download.png')
lbll=Label(tk)
lbll.pack()
lbll.config(image=gra)   #於執行階段重新指派
tk=mainloop()