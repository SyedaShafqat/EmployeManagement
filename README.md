# Employee Management System

This program is an Employee Management System (EMS) implemented in Python. It allows users to add new employees, display employee details, and save employee data to a file for future reference.

## Classes

### `Employee`

- Represents an employee with attributes such as Employee ID, Name, Position, and Salary.

### `AddEmploye`

- Subclass of `Employee` responsible for managing employees.
- Attributes:
  - `file_name`: The name of the file to save employee data (default is "employee.txt").
  - `employees`: List to store employee objects.

- Methods:
  - `append_employee(id, name, position, salary)`: Adds a new employee to the system and saves the data to the file.
  - `display_employee()`: Displays the details of all employees in the system.
  - `datasavetofile()`: Saves the employee data to the file.

## Main Functionality

1. **Add a New Employee**: Prompts the user to input Employee ID, Name, Position, and Salary, then adds the employee to the system and saves the data to the file.

2. **Display Employee Details**: Prints the details of all employees stored in the system.

3. **Exit the Program**: Exits the program loop.

## Usage

1. Run the program.
2. Choose from the menu options to add a new employee, display employee details, or exit the program.

## Usage Example

Employee Management System


**Add a new employee**

**Display employee details**

**Exit**

Enter your choice: 1

Enter Employee ID: 1001

Enter Name: John Doe

Enter Position: Manager

Enter Salary: 50000

Employee added successfully!

