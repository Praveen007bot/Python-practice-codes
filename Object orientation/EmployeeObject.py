class Employee:
    company_name  ='code'  # class based variable.
    def __init__(self, name, age, desg):
        self.name = name
        self.age = age
        self.desg = desg
    
    def login(self, time):
        print(self.name, "this employee logged in at", time)
    
    def logout(self, time):
        print(self.name, "this employee logged out at", time)

    def work(self, hours):
        print(f'{self.name} worked for {hours}')
    
    def getDetails(self):
        print(f'Employee name: {self.name}')
        print(f'Employee age: {self.age}')
        print(f'Employee designation: {self.desg}')

e1 = Employee("praveen", 22, "developer")
e1.getDetails()
e1.login("09:00")
e1.work(8)
e1.logout("05:00")

e2 = Employee("kumar", 22, "tester")
e2.getDetails()
e2.login("10:00")
e2.work(5)
e2.logout("03:00")