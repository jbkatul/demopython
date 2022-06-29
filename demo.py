class Employee:
    company_name = 'JBK'  # class/static variable

    def __init__(self, nm, id, sal):
            self.name = nm
            self.E_ID = id
            self.salary = sal

    def get_info(self):
            print(f"""Name of the employee is {self.name}
                        Id of EMployee is {self.E_ID} and
                    Salary is {self.salary}. """)

    def set_salary(self, s):
        if s > 0 and self.salary < s:
            self.salary = s
            print(f'Salary of employee {self.name} is updated to {self.salary}')
        else:
            print('Salary value must me greater than old one')
    
    @classmethod
    def get_cname(cls):
        print('Name of the company is',cls.company_name)



e1 = Employee('JAY', 101, 22000)
e1.get_cname()
Employee.get_cname()