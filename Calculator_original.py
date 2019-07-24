#
from tkinter import *
root=Tk()
operator=""
text_input=StringVar() #


#Function for arthmetic operator + - * & / No repetition are allowed
def sign_operator(number):
    global operator
    if (operator[-1]=="+"or operator[-1]=="-" or operator [-1]=="*" or operator[-1]=="/" or operator[-1]=="%"):
        operator=operator[0:-1]+str(number)
        text_input.set(operator)
    else:
        operator=operator+str(number)
        text_input.set(operator)
#Function to received Number clicked receive as string and concate
def whenclicked(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
#Function to clear the screen global variable operator will be zero
def whenzero(numbers):
    global operator
    if(len(operator)>0):

        operator=operator+str(numbers)
        text_input.set(operator)


def when_clear():
    global operator
    operator =""
    text_input.set("")
# Function to do arthmetic operator eval function is used to do arthmetic Function
def equalsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

#Function to connect my face book site
def connect_krish():
    import webbrowser #Module to Open Web
    webbrowser.open('www.facebook.com/krishdb38', new=2,autoraise=True) #new 2 is for new tab

#  For Window Logo, size , text############################
icon=PhotoImage(file="kor.gif")
root.tk.call("wm","iconphoto",root._w,icon)
root.title("By Krishna 크리스나")
root.geometry("350x515")
root.resizable(0,0)
#############################################################

# Main Display Part of Calculator
main_Entry=Entry(root,textvariable=text_input,bd=8,font=("arial",30,"bold"),insertwidth=20,bg="lightblue",width=15,selectborderwidth=5,  justify="right").grid(columnspan=4,)
#justify write from Left,
#===============================================================================================================================
# Button Line = 7 , 8, 9, *
btn7=Button(root,text="7",font=("arial",20,"bold"),command=lambda:whenclicked(7),bd=8,pady=16,  padx = 16,bg="pink",).grid(row=1,column=0)
# Button 8
btn8=Button(root,text="8",font=("arial",20,"bold"),command=lambda:whenclicked(8),bd=8,pady=16, padx = 16,bg="pink",).grid(row=1,column=1)
#Button 9
btn9=Button(root,text="9",font=("arial",20,"bold"),command=lambda:whenclicked(9),bd=8,pady=16, padx = 16,bg="pink",).grid(row=1,column=2)
#Button
btn_pls=Button(root,text="+",font=("arial",20,"bold") ,command=lambda:sign_operator("+"),bd=8,pady=16, padx = 16,bg="green",).grid(row=1,column=3)

 #=============================================================================================================================

# Button Line = 4, 5, 6, Minus
btn4=Button(root,text="4",font=("arial",20,"bold"), command=lambda:whenclicked(4),bd=8,pady=16, padx = 16,bg="lightblue",).grid(row=2,column=0)
# Button 8
btn5=Button(root,text="5",font=("arial",20,"bold") ,command=lambda:whenclicked(5),bd=8,pady=16,padx = 16,bg="lightblue",).grid(row=2,column=1)
#Button 9
btn6=Button(root,text="6",font=("arial",20,"bold"),command=lambda:whenclicked(6),bd=8,pady=16, padx = 16,bg="lightblue",).grid(row=2,column=2)
#Button
btn_minus=Button(root,text="--",font=("arial",20,"bold") ,command=lambda:sign_operator("-"),bd=8,pady=16, padx = 16,bg="purple",).grid(row=2,column=3)

#===============================================================================================================================
 #=============================================================================================================================

# Button Line = 1, 2, 3, *
btn1=Button(root,text="1",font=("arial",20,"bold")   ,command=lambda:whenclicked(1),bd=8,pady=16, padx = 16,bg="skyblue",).grid(row=3,column=0)
# Button 1
btn2=Button(root,text="2",font=("arial",20,"bold"),command=lambda:whenclicked(2),bd=8,pady=16, padx = 16,bg="skyblue",).grid(row=3,column=1)
#Button 2
btn3=Button(root,text="3",font=("arial",20,"bold")  ,command=lambda:whenclicked(3),bd=8,pady=16, padx = 16,bg="skyblue",).grid(row=3,column=2)
#Button  3
btnmultiply=Button(root,text="X",font=("arial",20,"bold"),command=lambda:sign_operator("*"),bd=8,pady=16, padx = 16,bg="blue",).grid(row=3,column=3)
 # Multiply
 #=============================================================================================================================

# Button Line = 0 , Clear, Total and division *
btn0=Button(root,text=0,font=("arial",20,"bold") ,command=lambda:whenzero(0),bd=8,pady=16, padx = 16,bg="lightblue",).grid(row=4,column=0)
# Button 8
btn_clear=Button(root,text="C",font=("arial",20,"bold") ,command=when_clear,bd=8,pady=16, padx = 16,bg="red",).grid(row=4,column=1)
#Button 9
btn_Equal=Button(root,text="=",font=("arial",20,"bold"),command=equalsInput ,bd=8,pady=16, padx = 16,bg="lightblue",).grid(row=4,column=2)
#Button
btn_division=Button(root,text="÷",font=("arial",20,"bold") ,command=lambda:sign_operator("/"),bd=8,pady=16, padx = 16,bg="yellow",).grid(row=4,column=3)
 #=============================================================================================================================
button_connect=Button(root,text="Say Hi to Krishna",font=("arial",20,"bold"),fg="blue",bg="skyblue",width=20,command=connect_krish).grid(columnspan=4)
root.mainloop()
