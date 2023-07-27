from tkinter import *

tk = Tk()

# 載入圖片
image = PhotoImage(file="download.png")

# 創建一個Label來顯示文字和圖片
label = Label(tk, text="CUTE!", image=image, compound='bottom')
label.pack()

tk.mainloop()


