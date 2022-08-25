class Employee:
    def __init__(self,fname,lname,city):
        self.firstname=fname
        self.lastname=lname
        self.city=city

    def getname(self):
         return self.firstname[0]+ self.lastname[0]+self.city[0]

    def fullname(self):
        return self.firstname,self.lastname,self.city


