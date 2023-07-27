def funct():
    print('hi')
    
funct()

def abc1():
    print('no input no output')
    
def abc(x):
    print(f'its fetching x={x} no output')
    
def abc3():
    return "its a string return from function as output"

def abc4(x,y):
    return x*2,y+x+y

a=abc1()
print(a)

a4 = abc4(5,8)
print(a4)

a41,a42 = abc4(5,8)
print(a41)
print(a42)

abc4(y=5,x=8)
abc4(5,y=8)

def abc5(x=1,y=0):
    return x+2,y+x+y

print(abc5())
print(abc5(4))
print(abc5(5,4))

def abc6(x,y=0,*p,**q):
    print(x*2,y+x+y)
    print(p)
    print(q)
    print('')
    
abc6()
abc6(5,4)
abc6(5,4,9,10,34,456,'hi,x=23')
abc6(5,4,9,10,34,456,'hi',m=23,n=[4,7,8]) 
abc6(5,4,9,10,34,456,'hi',p=23,q=[4,7,8])



### try-except-else-finally
try:
    a = 10
    b = int(input('Enter a number'))
    print(a/b)
except ValueError as err:
    print(err)
    print(a)
except ZeroDivisionError as err:
    print(err)
    print(a)
else:
    print('Sab badhiya')
finally:
    print('mar ja')
    
print('kham ho gaya')


a = 10
def xyz():
    global a 
    a += 20
    print(a)
    
print(a)
xyz()

def abc(x,y):
    return x+y
k=abc

abc

k

def pot():
    print('pot')
    
def pqr(f):
    f()
    
pqr(pot)

def basket():
    def dox():
        print('nox')
    dox()
    
basket()

def awesome(f,m,n):
    return f,m+n
    
p, _ =awesome(pot,3,4)
p()

# Decorator
def decorate(f):
    def special():
        print('ye toh special')
        f()
        print('Decorate done')
    return special
def prin(f):
    def specia():
        print('ye toh special')
        f()
        print('Decorate not done')
    return specia
@decorate
@prin
def simple():
    print('I am  not simple')
    
simple = decorate(simple)
simple()

### Annonymous Functions
# lamda expression
# lamda ip_args: op_args
def normal(x,y):
    return x * y
m = normal(4,5)
print(m)

normals = lambda x,y : x*y
normals(4,5)

def my_mapper(func,values):
    result = []
    for value in values:
        result += [func(value)]
    return result

data = [6,7,3,6,8,2]
print(my_mapper(lambda x:x*2, data))
print(my_mapper(lambda x:x*2 if x%2 else x/2, data))
print(my_mapper(lambda x:str(x),data))

def first(v):
    return v*2
def second(v):
    return v*2 if v%2 else v/2
def third(v):
    return str(v)
print(my_mapper(first,data))
print(my_mapper(second,data))
print(my_mapper(third,data))


    


   


   