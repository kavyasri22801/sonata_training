from leave import Leave
class RestrictedLeave(Leave):
    def __init__(self,empID,name,lbal,dob):
        super().__init__(empID,name,lbal)
        self.dob=dob

    def applyleave(self):
        return self.dob