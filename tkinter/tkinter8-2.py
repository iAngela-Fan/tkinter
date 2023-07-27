from tkinter import *
tk=Tk()
tk.geometry('300x50+50+70')
def s1(e):
    tk.title('1')
def s2(e):
    tk.title('2')
def s3(e):
    tk.title('3')
enyl=Entry(tk)
enyl.bind('1',s1)
enyl.bind('2',s2)
enyl.bind('3',s3)
enyl.pack()
tk.mainloop()