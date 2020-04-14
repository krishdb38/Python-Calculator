import tkinter as tk
window = tk.Tk()

v = tk.StringVar()
def show_choice():
    print(v.get())
tk.Label(window,text="Choose a Metrix for blastp",padx=20).pack()

tk.Radiobutton(window,text = "BLOSUM45",variable=v,value = "BLOSUM45",command = show_choice).pack(side = "left")
tk.Radiobutton(window,text = "BLOSUM62",variable = v,value="BLOSUM62",command = show_choice).pack(side = "left")
tk.Radiobutton(window,text = "BLOSUM82",variable = v,value="BLOSUM82",command = show_choice).pack(side = "left")

window.mainloop()