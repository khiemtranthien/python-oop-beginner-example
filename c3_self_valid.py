class Employee:
    # define method without "self" arg
    def employeeDetails(self):
        # this is instance variable
        self.name = "John"
        print("Employee name: ", self.name)

        # this is local variable
        age = 30
        print("Age: ", age)

    def printEmployeeDetails(self):
        print("Print employee details again:")
        print("Employee name: ", self.name)
        # this will cause the error because "age" only available in "employeeDetails"
        print("Age: ", age)


if __name__ == '__main__':
    employee1 = Employee()
    # it will throw an exception
    employee1.employeeDetails()
    # because behine the scence, Python interpreter will convert to:
    Employee.employeeDetails(employee1)

    employee1.printEmployeeDetails()
