class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

emp = Employee(30000)

print("Salary:", emp.get_salary())
