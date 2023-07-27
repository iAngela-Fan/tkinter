from tkinter import *
root=Tk()
root.title('repeat')
def show():
    lbll['text']=eval(enyl.get())  #可計算輸入內容
enyl=Entry(root)
enyl.insert(1,'calculater')
lbll=Label(root,text='Hello')
btnl=Button(root,text='start', command=show)
enyl.pack()
lbll.pack()
btnl.pack()
root.mainloop()

