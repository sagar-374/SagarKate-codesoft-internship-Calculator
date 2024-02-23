from tkinter import *

opstatus = 0
numstatus = 0
equation=""

def show(string):
    global equation
    if len(list(content.get())) == 0:
        equation=""
    if content.get().upper()=='ERROR':
        equation=''
    equation+=string
    mis_label.config(text="", justify=LEFT)
    content.set("{}".format(equation))

def fillclear():
    global equation
    equation=""
    content.set("")
    mis_label.config(text="")

def fillback():
    global equation
    back_str = list(content.get())
    if content.get().upper()=='ERROR':
        content.set("")
    elif len(back_str) > 0:
        back_str.pop()
        final_str = ""
        for i in back_str:
            final_str += i
        content.set(final_str)
        mis_label.config(text="")
        equation = final_str

def filltotal():
    global equation
    result=""
    mis_label.config(text=equation, anchor="e", justify=LEFT)
    if equation != "":
        try:
            result=eval(equation)
        except:
            result="ERROR"
            equation=""
            mis_label.config(text="")
        content.set("{}".format(result))
        equation=str(result)

#------TK------------------------
root = Tk()
root.geometry("309x410")
root.resizable(False,False)
root.title("Calculator")
root.config(bg="black")
content = StringVar()
#-------Dispaly portion----------
mis_label=Label(root, width=31, height=1, text="", bg="black", fg="white", font=("courier new",9))
mis_label.place(x=10,y=7)
text_area = Entry(root, width="12", textvariable=content, font=("courier new",23)).place(x=10,y=31)
#---------Numeric Buttons--------
one = Button(root, text="1", width=7,height=2, bg="gray", command=lambda: show("1")).place(x=10,y=280)
two = Button(root, text="2", width=7, height=2, bg="gray", command=lambda: show("2")).place(x=85,y=280)
three = Button(root, text="3", width=7, height=2, bg="gray", command=lambda: show("3")).place(x=160,y=280)
four = Button(root, text="4", width=7, height=2, bg="gray", command=lambda: show("4")).place(x=10,y=215)
five = Button(root, text="5", width=7, height=2, bg="gray", command=lambda: show("5")).place(x=85,y=215)
six = Button(root, text="6", width=7, height=2, bg="gray", command=lambda: show("6")).place(x=160,y=215)
seven = Button(root, text="7", width=7, height=2, bg="gray", command=lambda: show("7")).place(x=10,y=150)
eight = Button(root, text="8", width=7, height=2, bg="gray", command=lambda: show("8")).place(x=85,y=150)
nine = Button(root, text="9", width=7, height=2, bg="gray", command=lambda: show("9")).place(x=160,y=150)
zero = Button(root, text="0", width=7, height=2, bg="gray", command=lambda: show("0")).place(x=85,y=345)
clear = Button(root, text="C", width=7, height=2, bg="orange", command=fillclear).place(x=85,y=85)
dot = Button(root, text=".", width=7, height=2, bg="gray", command=lambda: show(".")).place(x=10,y=345)
#---------Buttons----------------
div = Button(root, text="/", width=7, height=2, bg="green", command=lambda: show("/")).place(x=235,y=85)
mul = Button(root, text="", width=7, height=2, bg="green", command=lambda: show("")).place(x=235,y=280)
sub = Button(root, text="-", width=7, height=2, bg="green", command=lambda: show("-")).place(x=235,y=215)
add = Button(root, text="+", width=7, height=2, bg="green", command=lambda: show("+")).place(x=235,y=150)
back = Button(root, text="<-", width=7, height=2, bg="orange", command=fillback).place(x=160,y=85)
total= Button(root, text="=", width=16, height=2, bg="cyan", command=filltotal).place(x=160,y=345)

root.mainloop()