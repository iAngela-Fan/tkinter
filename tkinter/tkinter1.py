from tkinter import *
tk=Tk()
tk.title('Welcome')             #視窗名稱
tk.geometry('200x200+50+70')    #視窗位置與大小

lbll=Label(tk,text='hello', font=('Arial', 18))    #標籤元件（輸出入說明）
lbll.pack()
tk.mainloop()