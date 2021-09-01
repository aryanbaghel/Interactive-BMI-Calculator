from tkinter import *

root=Tk()
root.title("Calcualtor")

e=Entry(root)
e.grid(row=0,column=0,columnspan=4,padx=40,pady=10)


def button_click(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))

def button_clear():
    e.delete(0,END)
    
    
def button_add():
    number_1=e.get()
    global f_num
    global maths
    maths="addition"
    f_num=int(number_1)
    e.delete(0,END)
    
    
def button_equal():
    global number_2
    number_2=e.get()
    e.delete(0,END)    
    
    if maths=="addition":
        e.insert(0,f_num + int(number_2))
        
    elif maths=="multiplication":
        e.insert(0,f_num * int(number_2))
        
        
    elif maths=="divide":
        e.insert(0,f_num / int(number_2))
    
    
    elif maths=="minus":
        e.insert(0,f_num - int(number_2))
    
def button_multiply():
    number_1=e.get()
    global f_num
    global maths
    maths="multiplication"
    f_num=int(number_1)
    e.delete(0,END)



def button_divide():
    number_1=e.get()
    global f_num
    global maths
    maths="divide"
    f_num=int(number_1)
    e.delete(0,END)



def button_minus():
    number_1=e.get()
    global f_num
    global maths
    maths="minus"
    f_num=int(number_1)
    e.delete(0,END)
    

button_1=Button(root,text="1",padx=43,pady=40,command=lambda: button_click(1),bg="black",fg="green")
button_2=Button(root,text="2",padx=40,pady=40,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=40,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=43,pady=40,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=40,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=40,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=43,pady=40,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=40,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=40,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=40,command=lambda: button_click(0))


button_c=Button(root,text="Clear",padx=79,pady=40,command=button_clear)
button_m=Button(root,text="=",padx=191,pady=40,command=button_equal)

button_p=Button(root,text="+",padx=43,pady=40,command=button_add)
button_multiply=Button(root,text="*",padx=45,pady=40,command=button_multiply)
button_divide=Button(root,text="/",padx=45,pady=40,command=button_divide)
button_minus=Button(root,text="-",padx=45,pady=40,command=button_minus)


button_1.grid(row="3",column="2")
button_2.grid(row="3",column="1")
button_3.grid(row="3",column="0")
button_4.grid(row="2",column="2")
button_5.grid(row="2",column="1")
button_6.grid(row="2",column="0")
button_7.grid(row="1",column="2")
button_8.grid(row="1",column="1")
button_9.grid(row="1",column="0")
button_0.grid(row="4",column="0")


button_c.grid(row=4,column=1,columnspan=2)
button_m.grid(row=5,column=0,columnspan=4)
button_p.grid(row=4,column=3)
button_multiply.grid(row=1,column=3)
button_divide.grid(row=2,column=3)
button_minus.grid(row=3,column=3)



root.mainloop()





