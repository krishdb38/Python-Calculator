from tkinter import filedialog
import tkinter as tk


def browse_button():
    """ Allow user to select a directory and store it in global var
        variable_name = folder_path
    """

    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return filename

window = tk.Tk()
folder_path = tk.StringVar()
lbl1 = tk.Label(window, textvariable = folder_path)
lbl1.grid(row =0, column =3)

button2 = tk.Button(text = "Species",command = browse_button)
button2.grid(row=0,column=0)

window.mainloop()