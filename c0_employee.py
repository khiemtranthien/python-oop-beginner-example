class Employee:
    name = "Ben"
    designation = "Sale Executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek > 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

if __name__ == '__main__':
    employee1 = Employee()
    employee1.hasAchievedTarget()
