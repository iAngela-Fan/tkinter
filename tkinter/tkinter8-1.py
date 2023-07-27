from tkinter import *
tk=Tk()
tk.geometry('200x50+50+70')
def show(e):
    tk.title('OK')
btn1=Button(tk,text='start')
btn1.bind('<Button-1>',show)
btn1.pack()
tk.mainloop()