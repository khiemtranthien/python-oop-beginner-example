class Employee:
    # this is called class variable, it keeps the value for all objects
    working_hours = 40


if __name__ == '__main__':
    employee1 = Employee()
    print(employee1.working_hours)

    employee2 = Employee()
    print(employee2.working_hours)

    # change working_hours will affect all objects
    Employee.working_hours = 45
    print(employee1.working_hours)
    print(employee2.working_hours)

    # "name" is call instance attribute
    employee1.name = 'John'
    print(employee1.name)

    # call "name" in employee2 will cause the error, because "name" belongs to
    # employee1 only
    try:
        print(employee2.name)
    except AttributeError as e:
        print(e)

    # what if I change the working_hours on employee1 directly
    employee1.working_hours = 50
    # it now becomes 50, because "working_hours" has become instance attribute
    print(employee1.working_hours)
    # it is still 45, "working_hours" is still class attribute
    print(employee2.working_hours)
