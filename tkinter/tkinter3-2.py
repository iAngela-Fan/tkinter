from tkinter import *
tk=Tk()
gra=PhotoImage(file='download.png')
lbll=Label(tk)
lbll.pack()
a=966815735
lbll.config(text=str(a))   #於執行階段重新指派
tk=mainloop()