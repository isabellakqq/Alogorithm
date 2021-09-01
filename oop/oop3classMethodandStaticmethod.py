class Employee:
    '''
    class methods: @classmethod cls

    
    '''
    raise_amount = 1.04 
    num_of_emps = 0 #class variable

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        #return new employee object
        return cls(first, last, pay)
emp_1 = Employee('Isabella', 'Kang', 9000)
emp_2 = Employee('Trey', 'Zhou', 20000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe_90000'

# first, last, pay = emp_str_1.split('-')
# #ceate a new employee
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_str(emp_str_1)
print(new_emp_1.pay)
print(new_emp_1.email)

print(max(4, 5))
