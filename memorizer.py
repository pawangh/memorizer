import tkinter
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title(" multiple factors ")

b1=tkinter.Button(screen,text="            open       ")
b2=tkinter.Button(screen,text="delete")
b3=tkinter.Button(screen,text="save")
b4=tkinter.Button(screen,text="add")

b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=3)

screen.mainloop()