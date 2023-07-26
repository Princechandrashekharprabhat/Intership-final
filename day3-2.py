a=30;b=40;c=39
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
    
a=30
while a > 0:
    print('hello')
    a=a-7
    if a==16:
        continue
    print('go')
else:
    print('oh')
    
a=[3,4,5,6]
for i in a:
    print(i,i*10)
    
for i in range(1,6):
    print(i * '*')

a[3,4,5,6,7,8,9,10]
# b=[]
b=b+[i*2]
for b in a:
    b.append(i*2)
print(b)

b1=[i*2 for i in a]
print(b1)

b2=[i for i in a if i%2==1]
print(b2)

num=36
print('odd')if num%2 else print('even')

a=[2,3,5,7,5,4,3]
b3=[f'{i} odd'if i%2 else f'{i} Even'for i in a]
print(b3)

{i:i**2 for i in a}
(i**2 for i in a)


    
    
    