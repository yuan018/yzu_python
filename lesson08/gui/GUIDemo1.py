import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label1 = tkinter.Label(win, text = 'Hi')
label1.grid(column=0, row=0)
label2 = tkinter.Label(win, text = 'FUUUU')
label2.grid(column=2, row=2)
button1 = tkinter.Button(win, text = 'None')
button1.grid(column=1, row=1)

win.geometry('300x300')

win.mainloop()