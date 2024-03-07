from tkinter import *
from subprocess import call

root = Tk()
#button_9 = Button(label_key,text='9',height=3,width=5,font=('Helvetica','12'))
#button_9.grid(row=0,column=0)
class Calculator:
    def click_button(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""

    ''' def delete(self):
        self.operator = str(self.entry.delete(len(self.entry.get())-1))
    '''


    def evaluate(self):
        self.answer =eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)

    def __init__(self,master):

        self.operator = ""        
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=45 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='cyan',width=45,bd=20,insertwidth=4,justify='right',font=('arial',10,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=40)



        label_key = Label(root, height=15, width=30,bd=10,bg='white')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=15, bg='white')
        label_fkey.pack(fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='orange')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7', font=('Helvetica', '16'),command= lambda : self.click_button(7),bg='gray',fg='blue')
        button_7.pack()

        label_8 = Label(label_key, bg='orange')
        label_8.grid(row=0, column=1, padx=20)
        button_8 = Button(label_8, text='8', font=('Helvetica', '16'),command= lambda: self.click_button(8),bg='gray',fg='blue')
        button_8.pack()

        label_9 = Label(label_key, bg='orange')
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='9', font=('Helvetica', '16'),command= lambda: self.click_button(9),bg='gray',fg='blue')
        button_9.pack()

        label_4 = Label(label_key, bg='orange')
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4', font=('Helvetica', '16'),command= lambda: self.click_button(4),bg='gray',fg='blue')
        button_4.pack()

        label_5 = Label(label_key, bg='orange')
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5', font=('Helvetica', '16'),command= lambda: self.click_button(5),bg='gray',fg='blue')
        button_5.pack()

        label_6 = Label(label_key, bg='orange')
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6', font=('Helvetica', '16'),command= lambda: self.click_button(6),bg='gray',fg='blue')
        button_6.pack()

        label_1 = Label(label_key, bg='orange')
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='1', font=('Helvetica', '16'),command= lambda: self.click_button(1),bg='gray',fg='blue')
        button_1.pack()

        label_2 = Label(label_key, bg='orange')
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='2', font=('Helvetica', '16'),command= lambda: self.click_button(2),bg='gray',fg='blue')
        button_2.pack()

        label_3 = Label(label_key, bg='orange')
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='3', font=('Helvetica', '16'),command= lambda: self.click_button(3),bg='gray',fg='blue')
        button_3.pack()

        label_0 = Label(label_key, bg='orange')
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0', font=('Helvetica', '16'),command= lambda: self.click_button(0),bg='gray',fg='blue')
        button_0.pack()

        label_deci = Label(label_key, bg='orange')
        label_deci.grid(row=3, column=1, padx=10, pady=10)
        button_deci = Button(label_deci, text='.', font=('Helvetica', '16'),command= lambda: self.click_button('.'),bg='gray',fg='blue')
        button_deci.pack()

        label_equal = Label(label_key, bg='orange')
        label_equal.grid(row=3, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=', font=('Helvetica', '16'),command= self.evaluate,bg='gray',fg='blue')
        button_equal.pack()

        label_C = Label(label_fkey, bg='orange')
        label_C.grid(row=0, column=0,columnspan=2)
        button_C = Button(label_C, text='C', font=('Helvetica', '16'), height=1, width=10,command=  self.clear,bg='gray',fg='blue')
        button_C.pack(side=LEFT)

        '''label_del = Label(label_fkey, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()'''
        
        call(["python", "PySimpleGUIWeb\\PyGUI.py"])
        label_sub = Label(label_fkey, bg='orange')
        label_sub.grid(row=1, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='-', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('-'),bg='gray',fg='blue')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='orange')
        label_mul.grid(row=1, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('*'),bg='gray',fg='blue')
        button_mul.pack()

        label_div = Label(label_fkey, bg='orange')
        label_div.grid(row=2, column=0, sticky=W)
        button_div = Button(label_div, text='/', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('/'),bg='gray',fg='blue')
        button_div.pack()

        label_add = Label(label_fkey, bg='orange')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('+'),bg='gray',fg='blue')
        button_add.pack()

        label_lbrace = Label(label_fkey, bg='orange')
        label_lbrace.grid(row=3,column=0,sticky=W,pady=10)
        button_lbrace = Button(label_lbrace,text='(', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('('),bg='gray',fg='blue')
        button_lbrace.pack()

        label_rbrace = Label(label_fkey, bg='orange')
        label_rbrace.grid(row=3, column=1, sticky=E, pady=10)
        button_rbrace = Button(label_rbrace, text=')', font=('Helvetica', '16'), height=1, width=3,
                               command=lambda: self.click_button(')'),bg='gray',fg='blue')
        button_rbrace.pack()

c = Calculator(root)
root.title("Python Calculator Challenge")
root.mainloop()