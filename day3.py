a=10
b=10.0
c=10+0j
d='hello'
e=[3,6,2]
f=(3,6,2)
g={'a':[45,6],'b':[1,6,2]}
h={5,2,8}
i=True
a.real

#string function
print(d.count['a'])
print(d.index('e'))
print(d.find('a'))
print(d.split('l'))
print(d.strip('l'))
print(d.replace('e','l'))
print(d.join('Wow'))
print(d.upper())
print(d.lower())
print(d.islower())
print(d.isupper())
print(d.isalpha())

'hi this is'.split('i')
' hi this is '.strip()
'good'.join('morning')
'-'.join('HELLO')
'wow'.join(['hi','there','to','now'])

days=10
s="last %d days" %(days)
print(s)
days=10
s=f"last {days}days"%(days)
print(s)

s='this will last atmost {} days'
days=10
s=s.format(days)
print(s)

s='this will last at most {1} days in {1} and extra {0}'
days=10
extra=5
s=s.format(days,extra)
print(s)

type(e)
#list function
e.append(50)
print(e)
print(e.count(10))
e.extend([4,6,2,3])
print(e)
print(e.index(4))
e.insert(2,100)
print(e)
print(e.pop())
print(e)
e.remove()
print(e)
e.sort()
print(e)
e1=e.copy()
e2=e
print(e)

# shallow copy vs deep copy
e1,e2
e2.append(1000)
print(e)
print(e1)
e2,e

#tupple function
print(f)
print(f.index(3))
print(f.count(3))

#Dictionary
print(g)
print(g.keys())
print(g.values())
print(g.get('a'))
print(g.pop('b'))
print(g.update({'c':34}))
print(g)

print(h)
h.add(50)
print(h)
print(h.intersection({2,10}))
print(h.pop())
print(h.remove(50))
print(h.union({10,20,30,40}))

#Type CONVERSION
float(a)
str(a)
int(float(30.4))
eval('45')
list(d)
tuple(d)
str(e)
dict(b=e)
set(e)
[*e1,*e2]
(*e1,*e2)
g1={'a':4,'b':[5,6]}
g2={'c':34,'a':34}
g1.update(g2)
g1
{**g1,**g2}
