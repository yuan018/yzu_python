import tkinter

def myadd():
    num.set(num.get() + 1)

def myexit():
    win.quit()

win = tkinter.Tk()  #視窗要先定義
win.geometry('300x300')

num = tkinter.IntVar()
num.set(0)

label = tkinter.Label(win, textvariable=num)
label.pack()

button = tkinter.Button(win, text='Add', command=myadd)
button.pack()

button2 = tkinter.Button(win, text='Exit', command=myexit)
button2.pack()

win.mainloop()