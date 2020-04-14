import tkinter as tk

window = tk.Tk()

v = tk.IntVar()
v.set(2) # Default is BLOSUM62

matrix = [("BLOSUM45",1),
("BLOSUM62",2),
("BLOSUM82",3)]

def show_choice():
    print(v.get())

tk.Label(window,text = "Choose a Matrix for blastp",padx = 20).pack()
for val,metrix_ in enumerate(matrix):
    tk.Radiobutton(window,text = metrix_,padx= 20,variable =v, command = show_choice,value = val).pack()
window.mainloop()