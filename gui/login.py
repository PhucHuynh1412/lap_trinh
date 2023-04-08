from tkinter import *

def xin_chao():
    lbl.configure(text='Hello Phúc')

window = Tk()
window.title('Login')

lbl = Label(window, text='Hello everybody')
lbl.grid(column=0, row=0)


btn = Button(text='Click Me', command=xin_chao)
btn.grid(column=1, row=0)

window.mainloop()

