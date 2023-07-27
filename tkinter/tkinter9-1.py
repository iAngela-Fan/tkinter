from tkinter import *
root=Tk()
root.title('repeat')
def show():
    lbll['text']=enyl.get()
enyl=Entry(root)
enyl.insert(1,'Write here')
lbll=Label(root,text='Hello')
btnl=Button(root,text='start', command=show)
enyl.pack()
lbll.pack()
btnl.pack()
root.mainloop()

