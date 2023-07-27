from tkinter import *
tk=Tk()
enyl=Entry(tk)
enyl.insert(0,'01234')
enyl.delete(1,3)
enyl.insert(2,'ab')
enyl.insert(END, '+')
enyl.pack()
tk.mainloop()