class Employee:
    # this is instance method
    def employeeDetails(self):
        # this is instance variable
        self.name = "John"
        print("Employee name: ", self.name)

    # welcomMessage is static method
    @staticmethod
    def welcomMessage():
        print("Welcome to our organization")


if __name__ == '__main__':
    employee1 = Employee()
    employee1.employeeDetails()
    employee1.welcomMessage()
