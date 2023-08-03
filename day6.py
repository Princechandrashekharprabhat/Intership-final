class Abc:
    pass

x=Abc()
x

class Abc():
    a = 10
    b = 20
    def show(self):
        print(self.a, Abc.b)
        
x = Abc()
print(x)
x.show()

x.a

y = Abc()
z = Abc()

y.show()

z.show()

x.a = 45
y.a = 55
Abc.b = 100

x.show()
y.show()
z.show()

from typing import Any


class Abc():
    def __init__(self, a = 10, b = 20):
        self.a = a
        Abc.b = b
    
    def __str__(self) -> str:
        return "Hi"
    
    def __call__(self, *args, **kwds):
        return sum(args)
    
    def show(self):
        print(self.a, Abc.b)

x = Abc()
print(x)
y = Abc(a = 30)
z = Abc(a = 15)
x.show();y.show();z.show()
w = Abc(b = 30)
x.show();y.show();z.show();w.show()
x(5,8,2,5,7,4)

Abc().show()

class Pqr(Abc):
    def __init__(self, a=10, b=20):
        super().__init__(a, b)
    def simple(self):
        print('Its Simple')
    def show(self):
        print(self.a)

p = Pqr(a = 30,)
p.simple()
p.show()
p()

import tkinter as ktr

app = ktr.Tk(__name__)
app.geometry('400x400')
app.title('My First GUI')

# Label, Entry, Button -> Geometric Management/Placement
# pack(), grid(row=0,column=0), place(x=20, y= 20)
var1 = ktr.Variable()
var1.set('Initial Value')

# a = ktr.Label(app, text = 'Mera Pehla Text')
a = ktr.Label(app, textvariable=var1)
a.grid(row=0, column=1)

var2 = ktr.Variable()
ktr.Entry(app, textvariable=var2).grid(row=1,column=1)

def putText():
    var1.set(var2.get())
ktr.Button(app, text='Put', command=putText).grid(row=2,column=1)

# ktr.Label(app, text = 'Ye doosra tareeka hai').pack()
ktr.Label(app, text = 'Ye doosra tareeka hai').grid(
    row = 3, column = 0
)

app.mainloop()