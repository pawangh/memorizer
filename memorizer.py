import tkinter
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title(" multiple factors ")

def add():
    edd=e1.get()
    lb.insert(tkinter.END,edd)
    e1.delete(0,tkinter.END)

b1=tkinter.Button(screen,text="open")
b2=tkinter.Button(screen,text="delete")
b3=tkinter.Button(screen,text="save")
b4=tkinter.Button(screen,text="add",command=add)
e1=tkinter.Entry(screen)
lb=tkinter.Listbox(screen)

b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=3)
e1.grid(row=2,column=1,columnspan=2)
lb.grid(row=3,column=1,columnspan=3)

screen.mainloop()