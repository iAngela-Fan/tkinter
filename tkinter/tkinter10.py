from tkinter import *
frm=Tk()

btn1=Button(frm, text='1', width=30)
btn2=Button(frm, text='2', width=10, height=2)
btn3=Button(frm, text='3', width=20)
btn4=Button(frm, text='4', width=20)

btn1.grid(row=0, column=0, columnspan=3)
btn2.grid(row=1, column=0, rowspan=3)
btn3.grid(row=1, column=2, columnspan=2)
btn4.grid(row=2, column=2, columnspan=2)

frm.mainloop()