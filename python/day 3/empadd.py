from employee import Employee
from address import Address

add1=Address('guntur', '52205')
add2=Address('banglore', '52205')
e1 = Employee("kavya", "sri", "hyd")
e2 = Employee("kavya", "sri",[add1, add2])
print(e1.fullname())
print(e1.getname())
print(e2.fullname())