import tkinter as tk
window = tk.Tk()

frame1 = tk.Frame(window,height = 100, width = 100,bg = "white",borderwidth = 2)
frame2 = tk.Frame(frame1,height = 100, width = 100,bg = "red",borderwidth = 2)
frame1.pack()
frame2.pack()

label = tk.Label(frame2, text = "label") # Receive a call back from button here
label.pack()
button = tk.Button(frame1, text = "Button") #Send some action to Label here
button.pack()

window.mainloop()