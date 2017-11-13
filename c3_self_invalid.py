class Employee:
    # define method without "self" arg
    def employeeDetails():
        pass


if __name__ == '__main__':
    employee1 = Employee()
    # it will throw an exception
    employee1.employeeDetails()
    # because behine the scence, Python interpreter will convert to:
    # Employee.employeeDetails(employee1)
