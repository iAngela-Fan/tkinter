from tkinter import *
tk=Tk()
gra=PhotoImage(file='m1.gif')
grb=[]
for i in range(5):
    grb.append(PhotoImage(file='m'+str(i)+'.gif'))
lbl0=Label(tk,image=gra)
lbl0.pack(side=LEFT)
lbl1=Label(tk,image=gra)
lbl1.pack(side=LEFT)
lbl2=Label(tk,image=gra)
lbl2.pack(side=LEFT)
lbl3=Label(tk,image=gra)
lbl3.pack(side=LEFT)
lbl4=Label(tk,image=gra)
lbl4.pack(side=LEFT)


a=[lbl0, lbl1, lbl2, lbl3, lbl4]
for i in range(5):
    a[i].config(image=grb[i])
tk=mainloop()


