import tkinter
from tkinter import ttk
from tkinter import messagebox

def sumbit():
    messagebox.showinfo('結帳資訊', "0".format(combo.get()))

win = tkinter.Tk()
win.geometry('400x300')

label = tkinter.Label(win, text='品項 : ')
#fruits = ['apple', 'banana', 'mango', 'melonwater']
fruits = {'apple':50, 'banana':60, 'mango':70, 'melonwater':25}
combo = ttk.Combobox(win, values=list(fruits.keys()), state="readonly") # readonly, disabled
combo.current(2)
label2 = tkinter.Label(win, text='甜度 : ')

rdio1 = tkinter.Radiobutton(win, text='正常', value=1.0)
rdio2 = tkinter.Radiobutton(win, text='少糖', value=0.7)
rdio3 = tkinter.Radiobutton(win, text='半糖', value=0.5)
rdio4 = tkinter.Radiobutton(win, text='微糖', value=0.3)
rdio5 = tkinter.Radiobutton(win, text='無糖', value=0)

#對話視窗
chk1 = tkinter.Checkbutton(win, text='去冰')
chk2 = tkinter.Checkbutton(win, text='提袋')

#結帳
btn = tkinter.Button(win, text='結帳', command=sumbit)

# UI 布局
label.grid (column=0, row=0, padx=10, pady=10, sticky="w") #sticky:靠向 # w:西邊，同理E、S、N
combo.grid (column=0, row=0, padx=70, pady=10, sticky="w")
label2.grid(column=0, row=1, padx=10, pady=10, sticky="w")
rdio1.grid (column=0, row=1, padx=70, pady=10, sticky="w")
rdio2.grid (column=0, row=1, padx=130, pady=10, sticky="w")
rdio3.grid (column=0, row=1, padx=190, pady=10, sticky="w")
rdio4.grid (column=0, row=1, padx=250, pady=10, sticky="w")
rdio5.grid (column=0, row=1, padx=310, pady=10, sticky="w")
chk1.grid (column=0, row=2, padx=10, pady=10, sticky="w")
chk2.grid (column=0, row=2, padx=70, pady=10, sticky="w")
btn.grid (column=0, row=3, padx=10, pady=10, sticky="w")


win.mainloop()