class Employee:
    '''
    creat simple calsses 
    difference between a class and an instance
    '''
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{}, {}'.format(self.first, self.last)

        
emp_1 = Employee('Isabella', 'Kang', 9000)
emp_2 = Employee('Trey', 'Zhou', 20000)
print(emp_1.email)
print(Employee.fullname(emp_1))
print(emp_2.fullname())