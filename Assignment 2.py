from tkinter import *
import re
import math

class Mywindow:
    def __init__(self, master):
        self.expression = ""
        
        self.result_label = Label(master, font=("arial", 12, "bold"))
        self.result_label.place(x=10, y=10, width=240)
        
        self.b1 = Button(master, width=5, text="7",activebackground='#58F', command=lambda: self.button_click(7))
        self.b1.place(x=10, y=100)

        self.b2 = Button(master, width=5, text="8",activebackground='#58F', command=lambda: self.button_click(8))
        self.b2.place(x=70, y=100)

        self.b3 = Button(master, width=5, text="9", activebackground='#58F',command=lambda: self.button_click(9))
        self.b3.place(x=130, y=100)

        self.b4 = Button(master, width=5, text="4", activebackground='#58F',command=lambda: self.button_click(4))
        self.b4.place(x=10, y=150)

        self.b5 = Button(master, width=5, text="5", activebackground='#58F',command=lambda: self.button_click(5))
        self.b5.place(x=70, y=150)

        self.b6 = Button(master, width=5, text="6", activebackground='#58F',command=lambda: self.button_click(6))
        self.b6.place(x=130, y=150)

        self.b7 = Button(master, width=5, text="1",activebackground='#58F', command=lambda: self.button_click(1))
        self.b7.place(x=10, y=200)

        self.b8 = Button(master, width=5, text="2", activebackground='#58F',command=lambda: self.button_click(2))
        self.b8.place(x=70, y=200)

        self.b9 = Button(master, width=5, text="3", activebackground='#58F',command=lambda: self.button_click(3))
        self.b9.place(x=130, y=200)

        self.b20 = Button(master, width=5, text="0", activebackground='#58F',command=lambda: self.button_click(0))
        self.b20.place(x=10, y=250)
        
        self.b21 = Button(master, width=5, text=".", activebackground='#58F', command=lambda: self.button_click('.'))
        self.b21.place(x=70, y=250)


        self.add = Button(master, width=5, text="+",activebackground='#58F', command=lambda: self.operator_click('+'))
        self.add.place(x=190, y=200)

        self.sub = Button(master, width=5, text="-",activebackground='#58F', command=lambda: self.operator_click('-'))
        self.sub.place(x=190, y=150)

        self.mul = Button(master, width=5, text="*", activebackground='#58F',command=lambda: self.operator_click('*'))
        self.mul.place(x=190, y=100)

        self.div = Button(master, width=5, text="/",activebackground='#58F', command=lambda: self.operator_click('/'))
        self.div.place(x=190, y=50)
        
        self.root_btn = Button(master, width=5, text="√", activebackground='#58F', command=lambda: self.operator_click('sqrt'))
        self.root_btn.place(x=130, y=50)

        self.percent = Button(master, width=5, text="%", activebackground='#58F', command=lambda: self.operator_click('%'))
        self.percent.place(x=70, y=50)

        self.equal = Button(master, width=5, text="=", activebackground='#58F',command=self.calculate)
        self.equal.place(x=190, y=250)

        self.clear = Button(master, width=5, activebackground='#58F',text="Clear", command=self.clear)
        self.clear.place(x=10, y=50)
        
        self.backspace = Button(master, width=5, text="⌫", activebackground='#58F', command=self.remove_last)
        self.backspace.place(x=130, y=250)



    def button_click(self, number):
        self.expression += str(number)
        self.update_label()
        
    def operator_click(self, operator):
        if operator == 'sqrt':
            self.expression = str(math.sqrt(float(self.expression)))
        else:
            self.expression += operator
        self.update_label()

    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_label.config(text=str(result))
            self.expression = str(result)
        except Exception as e:
            self.result_label.config(text="Error")

    def clear(self):
        self.expression = ""
        self.update_label()

    def update_label(self):
        self.result_label.config(text=self.expression)
        
    def remove_last(self):
        self.expression = self.expression[:-1]
        self.update_label()

root = Tk()
root.title("CALCULATOR")
root.geometry("250x295")
root.config(bg="light green")

mywin = Mywindow(root)
root.mainloop()
