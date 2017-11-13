class Employee:
    def enterEmployeeDetails(self):
        # this is instance variable
        self.name = "John"

    def displayEmployeeDetails(self):
        print("Employee name: ", self.name)


if __name__ == '__main__':
    employee1 = Employee()
    # error will be thrown becaus "name" attribute has not been defined
    employee1.displayEmployeeDetails()
