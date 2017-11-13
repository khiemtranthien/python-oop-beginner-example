class Employee:
    # this is called class variable, it keeps the value for all objects
    working_hours = 40


if __name__ == '__main__':
    employee1 = Employee()
    print(employee1.working_hours)

    employee2 = Employee()
    print(employee2.working_hours)

    # change working_hours will affect all objects
    employee1.working_hours = 45
    print(employee1.working_hours)
    print(employee2.working_hours)
