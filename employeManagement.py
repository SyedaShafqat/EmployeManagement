class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary


class AddEmploye(Employee):
    def __init__(self, file_name: object = "employe.txt"):
        self.file_name = file_name
        self.employees = []

    def append_employee(self, id, name, position, salary):
        self.employees.append(Employee(id, name, position, salary))
        self.datasavetofile()

    def display_employee(self):
        if not self.employees:
            print('No Data Found')
        else:
            for employee in self.employees:
                print(f"Employee ID: {employee.id}")
                print(f"Name: {employee.name}")
                print(f"Position: {employee.position}")
                print(f"Salary: {employee.salary}\n")

    def datasavetofile(self):
        with open(self.file_name, "w") as file:
            for employee in self.employees:
                file.write(f"Employee ID: {employee.id}\n")
                file.write(f"Name: {employee.name}\n")
                file.write(f"Position: {employee.position}\n")
                file.write(f"Salary: {employee.salary}\n\n")


def main():
    add_employee = AddEmploye()

    while True:
        print("\nEmployee Management System")
        print("1. Add a new employee")
        print("2. Display employee details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            add_employee.append_employee(id, name, position, salary)
        elif choice == "2":
            add_employee.display_employee()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
