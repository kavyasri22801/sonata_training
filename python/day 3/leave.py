class Leave:
    def __init__(self, empID, name, lbal):
        self.employeeid = empID
        self.name = name
        self.leavebalance = lbal
    def applyleave(self):
        return self.employeeid, self.name, self.leavebalance