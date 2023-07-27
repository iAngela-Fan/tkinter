from tkinter import *
frm=Tk()

frm.title('calculator')

def add():
    lbl1['text']='+'
    lbl3['text']=str(int(eny1.get())+int(eny2.get()))
def sub():
    lbl1['text']='-'
    lbl3['text']=str(int(eny1.get())-int(eny2.get()))
def mul():
    lbl1['text']='x'
    lbl3['text']=str(int(eny1.get())*int(eny2.get()))
def div():
    lbl1['text']='/'
    lbl3['text']=str(int(eny1.get())/int(eny2.get()))
def divi():
    lbl1['text']='//'
    lbl3['text']=str(int(eny1.get())//int(eny2.get()))
eny1=Entry(frm, text=' ', width=10)
eny1.insert(1,'16')

lbl1=Label(frm, text=' ', width=10)   #如果text裡打相同的字會造成同步

eny2=Entry(frm, width=10)
eny2.insert(1,'5')

lbl2=Label(frm, text=' = ', width=10)
lbl3=Label(frm, text=' ', width=10)

btn1=Button(frm, text='+', width=10, padx=1, command=add)
btn2=Button(frm, text='-', width=10, padx=1, command=sub)
btn3=Button(frm, text='x', width=10, padx=1, command=mul)
btn4=Button(frm, text='/', width=10, padx=1, command=div)
btn5=Button(frm, text='//', width=10, padx=1, command=divi)
btn6=Button(frm, text='End', width=50, command=frm.destroy)

eny1.grid(row=0, column=0)
lbl1.grid(row=0, column=1)
eny2.grid(row=0, column=2)
lbl2.grid(row=0, column=3)
lbl3.grid(row=0, column=4)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=1, column=3)
btn5.grid(row=1, column=4)

btn6.grid(row=2, column=0, columnspan=5)
frm.mainloop()
