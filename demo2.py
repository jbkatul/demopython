class Employee:
    company_name = 'TCS'
    city = 'Pune'

    def __init__(self,nm,id,sal):
        self.name = nm
        self.E_ID = id
        self.salary = sal


e1 = Employee('Nayan', 101, 25000)
print(e1.name)
print(e1.E_ID)
print(e1.salary)
print(Employee.company_name)
print(e1.city)
e1.name = 'Nayan Baba'
print('new name of e1 is :',e1.name)