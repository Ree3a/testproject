from _ast import Lambda
from tkinter import *

root = Tk()
root.iconbitmap('Calculator_30001.ico')
root.title('Digital Calculator')
root.resizable(0,0)
e = Entry(root, width=22,justify="right", borderwidth=14, bg="gray", font=("Times New Roman", 20, "bold"), )
e.grid(row=2, column=0, columnspan=15, ipadx=10, ipady=10)


# defining the title of the project
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


# defining the button
button_1 = Button(root, text="1", padx=20, pady=10, fg="black", bg="silver",font=('Times New Roman', 20, "bold",),borderwidth=5,

                  command=lambda: button_click(1), )

button_2 = Button(root, text="2", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(2), )
button_3 = Button(root, text="3", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(3), )
button_4 = Button(root, text="4", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(4), )
button_5 = Button(root, text="5", padx=20, pady=10, fg="black", bg="silver", font=('Times New  Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(5), )
button_6 = Button(root, text="6", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(6), )
button_7 = Button(root, text="7", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(7), )
button_8 = Button(root, text="8", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(8), )
button_9 = Button(root, text="9", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(9), )
button_0 = Button(root, text="0", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                  borderwidth=5,
                  command=lambda: button_click(0), )
button_add = Button(root, text="+", padx=22, fg="black", bg="silver", pady=10, font=('Times New Roman', 20, "bold"),
                    borderwidth=5,
                    command=button_add, )
button_sub = Button(root, text="-", padx=22, pady=10, fg="black", bg="silver", font=('Times New Roman', 24, "bold"),
                    borderwidth=5,
                    command=button_sub, )
button_mult = Button(root, text="*", padx=22, pady=6, fg="black", bg="silver", font=('Times New Roman', 24, "bold"),
                     borderwidth=5,
                     command=button_mult, )
button_div = Button(root, text="/", padx=20, fg="black", bg="silver", pady=10, font=('Times New Roman', 22, "bold"),
                    borderwidth=5,
                    command=button_div, )
button_clear = Button(root, text="C", padx=20, fg="black", bg="silver", pady=10, font=('Times New Roman', 20, "bold"),
                      borderwidth=5,
                      command=button_clear, )
button_equal = Button(root, text="=", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                      borderwidth=5,
                      command= button_equal, )
button_esc = Button(root, text="Esc", padx=18, pady=10, fg="black", bg="silver", font=('Times New Roman', 19, "bold"),
                    borderwidth=5,
                    command=lambda:button_esc, )
button_per = Button(root, text="%", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                    borderwidth=5,
                    command=lambda: button_per, )
button_bracket = Button(root, text="()", padx=20, pady=10, fg="black", bg="silver", font=('Times New Roman', 20, "bold"),
                        borderwidth=5,
                        command=lambda: button_bracket, )
button_point = Button(root,text=".", padx=28, pady=10,fg="black", bg="silver",font=('Times New Roman', 20, "bold"), borderwidth=5,
                      command=lambda: button_point, )
# putting button on the screen
button_1.grid(row=3, column=0, )
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)

button_0.grid(row=6, column=0)
button_add.grid(row=3, column=3)
button_sub.grid(row=4, column=3)

button_mult.grid(row=5, column=3)
button_div.grid(row=6, column=1)
button_clear.grid(row=6, column=2)
button_esc.grid(row=6, column=3)

button_equal.grid(row=7, column=0, )
button_per.grid(row=7, column=2)
button_bracket.grid(row=7, column=1)
button_point.grid(row=7, column=3)
root.mainloop()
