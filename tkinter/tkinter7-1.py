from tkinter import *
tk=Tk()
tk.geometry('200x50+50+70')
def show():
    tk.title('OK')
btn1=Button(tk,text='start',command=show)
btn1.pack()
tk.mainloop()