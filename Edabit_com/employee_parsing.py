class Employee:
    def __init__(self, firstname, lastname, salary) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(self, str1):
        self.str1 = str1
        new_str1 = self.str1.split("-")
        self.firstname = new_str1[0]
        self.lastname = new_str1[1]
        self.salary = int(new_str1[2])
        return Employee

        

# emp1 = Employee("Terelle","Jack", 250000)
# print(emp1.salary)
# print(emp1.from_string("John-Smith-5000"))

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)