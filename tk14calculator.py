from cgitb import text
from tkinter import*
window=Tk()
window.title('Calculator')
window.geometry('380x290')
window.config(bg='black')
window.resizable(False,False)
input_text=StringVar()
var1=" "
def equal():
    global var1
    result=str(eval(var1))
    input_text.set(result)
    var1=" "
def clear():
    global var1
    var1=" "
    input_text.set(" ")
def button_click(item):
    global var1
    var1=var1+str(item)
    input_text.set(var1)
t1=Entry(window,width=55,fg='red',textvariable=input_text)
t1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
b7=Button(window,text=7,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(7))
b7.grid(row=1,column=0)
b8=Button(window,text=8,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(8))
b8.grid(row=1,column=1)
b9=Button(window,text=9,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(9))
b9.grid(row=1,column=2)
bdiv=Button(window,text='/',padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click('/'))
bdiv.grid(row=1,column=3)

b6=Button(window,text=6,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(6))
b6.grid(row=2,column=0)
b5=Button(window,text=5,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(5))
b5.grid(row=2,column=1)
b4=Button(window,text=4,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(4))
b4.grid(row=2,column=2)
bmul=Button(window,text='*',padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click('*'))
bmul.grid(row=2,column=3)




b1=Button(window,text=1,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(1))
b1.grid(row=3,column=0)
b2=Button(window,text=2,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(2))
b2.grid(row=3,column=1)
b3=Button(window,text=3,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(3))
b3.grid(row=3,column=2)
bsub=Button(window,text='-',padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click('-'))
bsub.grid(row=3,column=3)


bc=Button(window,text='C',padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:clear())
bc.grid(row=4,column=0)
b0=Button(window,text=0,padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click(0))
b0.grid(row=4,column=1)
bequal=Button(window,text='=',padx=40,pady=20,border=1,bg='red',fg='white',command=equal)
bequal.grid(row=4,column=2)
badd=Button(window,text='+',padx=40,pady=20,border=1,bg='black',fg='white',command=lambda:button_click('+'))
badd.grid(row=4,column=3)
window.mainloop()
