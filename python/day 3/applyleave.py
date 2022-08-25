from leave import Leave
from bol import BasketOfLeave
from rl import RestrictedLeave

l1=Leave(1234, "kavya", 20)
print(l1.applyleave())

l2=BasketOfLeave(2346, "rajasree", 50, "sick leave")
print(l2.applyleave())

l3=RestrictedLeave(2346, "kavya",50, 2000)
print(l3.applyleave())