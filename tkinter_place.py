import tkinter as tk
import tkinter.messagebox as tkMessageBox

window = tk.Tk()
def helloCallBack():
    tkMessageBox.showinfo("Hello Python","Hello World")

B = tk.Button(window, text= "hello", command = helloCallBack)
B.pack()
B.place(bordermode = 'outside',height = 200, width=100,x =10,y=30)
window.mainloop()