class Employee:
    '''
    class variable 
    check if the instance contains the attribute
    and if it doesn't the it will see if the calss and the class 
    inherits from contains that attibute so when we access 
    '''
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{}, {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

        
emp_1 = Employee('Isabella', 'Kang', 9000)
emp_2 = Employee('Trey', 'Zhou', 20000)
emp_1.apply_raise()
# print(emp_1.pay)
print(emp_1.__dict__)
# print(Employee.__dict__)
print(Employee.num_of_emps)