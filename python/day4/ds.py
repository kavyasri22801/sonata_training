
#using array
from array import *
a= array('i',[10,20,30,40,50])
print(type(a))
print(a)
print(a[0],a[1])
print(a[2:5])
print(a[:-1])
a.append(70)
print(a)
a.extend([90,60,50])
print(a)
print(len(a))


#using list
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(a.copy())
print(a.count(1))
print(a[3:7])
print(a[-4:-1])
print(a.remove(10))
print(a)
a.remove(9)

#usig dict
d={"name":"kavya","city":"guntur"}
print(type(d))
print(d.copy())
print(d.pop("city"))
print(d.get("name"))
print(d.clear())
print(d)
d.update({"phone":"456785757"})
print(d)

#using set
a=set((1,2,3,4,5,6,5))
b=set((6,4,2,6,8,2,4,4))
print(type(a))
print(a)
print(a.copy())
print(a.update(a,b))
print(a)
print(a.pop())
print(a)
c=a.insertion(b)
print(c)

#using tuple
a=(5,6,7,8,9,10)
print(type(a))
print(a.count(4))
print(a[2])
print(a[1:4])