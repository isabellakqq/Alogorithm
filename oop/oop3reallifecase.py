'''
staticmethod is not callable
Date.function(pram)
A class method can access or modify the class state while a static method can’t access or modify it.
'''
class Date:
    @staticmethod
    def is_workday(day):
        print(day.weekday())
        print(day)
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2021, 8, 30)
print(Date.is_workday(my_date))

