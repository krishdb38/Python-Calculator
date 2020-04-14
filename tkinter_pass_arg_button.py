import tkinter as tk
import webbrowser

# funciton
def openURL(x):
    new =2
    webbrowser.open(x,new = new)

# From Setup
window = tk.Tk()
window.geometry("350x350")
window.resizable(0,0)
window.title("")
