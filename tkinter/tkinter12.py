from tkinter import *
tk=Tk()
def show(s):
    a=enyl.get()
    if a=='0':
        enyl.delete(0, END)
    enyl.insert(END,s)

def clr():
    enyl.delete(0,END)
    enyl.insert(1,'0')

def cal():
    x=enyl.get()
    enyl.delete(0,END)
    enyl.insert(0,str(eval(x)))


enyl=Entry(tk, width=30)
enyl.insert(1,'0')
btn7=Button(tk, text='7', width=4, padx=1, command=lambda:show('7'))
btn8=Button(tk, text='8', width=4, padx=1, command=lambda:show('8'))
btn9=Button(tk, text='9', width=4, padx=1, command=lambda:show('9'))
btnd=Button(tk, text='/', width=4, padx=1, command=lambda:show('/'))
btn4=Button(tk, text='4', width=4, padx=1, command=lambda:show('4'))
btn5=Button(tk, text='5', width=4, padx=1, command=lambda:show('5'))
btn6=Button(tk, text='6', width=4, padx=1, command=lambda:show('6'))
btnx=Button(tk, text='x', width=4, padx=1, command=lambda:show('*'))
btn1=Button(tk, text='1', width=4, padx=1, command=lambda:show('1'))
btn2=Button(tk, text='2', width=4, padx=1, command=lambda:show('2'))
btn3=Button(tk, text='3', width=4, padx=1, command=lambda:show('3'))
btnm=Button(tk, text='-', width=4, padx=1, command=lambda:show('-'))
btn0=Button(tk, text='0', width=4, padx=1, command=lambda:show('0'))
btnc=Button(tk, text='C', width=4, padx=1, command=clr)
btne=Button(tk, text='=', width=4, padx=1, command=cal)
btnp=Button(tk, text='+', width=4, padx=1, command=lambda:show('+'))

enyl.grid(row=0, column=0, columnspan=5)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnd.grid(row=1, column=3)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnx.grid(row=2, column=3)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btnm.grid(row=3, column=3)
btn0.grid(row=4, column=0)
btnc.grid(row=4, column=1)
btne.grid(row=4, column=2)
btnp.grid(row=4, column=3)

tk.mainloop()