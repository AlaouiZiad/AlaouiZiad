import tkinter as tk


from math import *



def eval_calc():
    global exp
    try:
        txt_exp.delete(1.0,"end")
        txt_exp.insert(1.0,m_eval(exp))
        last_exp.delete(1.0,"end")
        last_exp.insert(1.0,exp)
        exp=str(m_eval(exp))
    except:
        txt_exp.delete(1.0,"end")
        txt_exp.insert(1.0,"Error")



def clr():
    global exp
    txt_exp.delete(1.0,"end")
    exp=""



def add(string):
    global exp
    txt_exp.insert("end",str(string))
    exp+=str(string)

def pclr():
    global exp
    txt_exp.delete(1.0,"end")
    exp=exp[:-1]
    txt_exp.insert(1.0,exp)

exp=""

root=tk.Tk()
root.geometry("300x275")
root.configure(background="black")

last_exp=tk.Text(root, height=1,background="black",border=0,foreground="white", width=16, font=("arial",12))
last_exp.grid(columnspan=4)




txt_exp=tk.Text(root, height=1,background="black",border=0,foreground="white", width=16, font=("arial",24))
txt_exp.grid(row=1,columnspan=7)



btn_1 = tk.Button(root, text="1", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(1), width=3, font=("Arial",14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(2), width=3, font=("Arial",14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(3), width=3, font=("Arial",14))
btn_3.grid(row=2, column=3)


btn_4 = tk.Button(root, text="4", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(4), width=3, font=("Arial",14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(5), width=3, font=("Arial",14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(6), width=3, font=("Arial",14))
btn_6.grid(row=3, column=3)


btn_7 = tk.Button(root, text="7", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(7), width=3, font=("Arial",14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(8), width=3, font=("Arial",14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(9), width=3, font=("Arial",14))
btn_9.grid(row=4, column=3)


btn_0 = tk.Button(root, text="0", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(0), width=3, font=("Arial",14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("+"), width=3, font=("Arial",14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("-"), width=3, font=("Arial",14))
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("*"), width=3, font=("Arial",14))
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("/"), width=3, font=("Arial",14))
btn_div.grid(row=5, column=4)


btn_open = tk.Button(root, text="(", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("("), width=3, font=("Arial",14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add(")"), width=3, font=("Arial",14))
btn_close.grid(row=5, column=3)


btn_clear = tk.Button(root, text="C", activebackground="grey",background="black",border=0,foreground="white",command=clr, width=3, font=("Arial",14))
btn_clear.grid(row=6, column=1, columnspan=2)


btn_partclear = tk.Button(root, text="←", activebackground="grey",background="black",border=0,foreground="white",command=pclr, width=3, font=("Arial",14))
btn_partclear.grid(row=6, column=2, columnspan=2)


btn_equals = tk.Button(root, text="=", activebackground="grey",background="black",border=0,foreground="white",command=eval_calc, width=3, font=("Arial",14))
btn_equals.grid(row=6, column=3, columnspan=2)


#scientifiq part

def m_eval(s):
    x=str(s)
    return eval(x.replace("√(","sqrt(").replace("%","/100").replace("^","**"))
    




btn_root = tk.Button(root, text="√", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("√("), width=3, font=("Arial",14))
btn_root.grid(row=2, column=5)

btn_percent = tk.Button(root, text="%", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("%"), width=3, font=("Arial",14))
btn_percent.grid(row=3, column=5)

btn_exp = tk.Button(root, text="^", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("^"), width=3, font=("Arial",14))
btn_exp.grid(row=4, column=5)


btn_sin = tk.Button(root, text="sin", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("sin("), width=3, font=("Arial",14))
btn_sin.grid(row=2, column=6)

btn_cos = tk.Button(root, text="cos", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("cos("), width=3, font=("Arial",14))
btn_cos.grid(row=3, column=6)

btn_tan = tk.Button(root, text="tan", activebackground="grey",background="black",border=0,foreground="white",command=lambda: add("tan("), width=3, font=("Arial",14))
btn_tan.grid(row=4, column=6)


root.mainloop()
