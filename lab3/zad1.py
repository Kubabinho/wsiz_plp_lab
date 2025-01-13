class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"

class EmployeesManager:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"employee added: {employee}")

    def list_employees(self):
        if not self.employees:
            print("no employees in the system")
        else:
            for emp in self.employees:
                print(emp)

    def remove_employees_by_age_range(self, min_age: int, max_age: int):
        before_removal = len(self.employees)
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        removed_count = before_removal - len(self.employees)
        print(f"deleted {removed_count} employees in age range of {min_age} to {max_age}")

    def find_employee_by_name(self, name: str):
        for emp in self.employees:
            if emp.name == name:
                return emp
        print(f"cant find employee: {name}")
        return None

    def update_employee_salary(self, name: str, new_salary: float):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            print(f"changed the employee salary from {name} to {new_salary}.")
        else:
            print(f"cant change salary, employee {name} doesnt exist.")

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\n--- Employees System ---")
            print("1. add employee")
            print("2. show employee lsit")
            print("3. delete employees in age range")
            print("4. change employee salary")
            print("5. exit")
            choice = input("choose ")

            if choice == "1":
                name = input("inpiut name ")
                age = int(input("input age "))
                salary = float(input("input salary "))
                self.manager.add_employee(Employee(name, age, salary))

            elif choice == "2":
                self.manager.list_employees()

            elif choice == "3":
                min_age = int(input("input min age "))
                max_age = int(input("input max age "))
                self.manager.remove_employees_by_age_range(min_age, max_age)

            elif choice == "4":
                name = input("input name ")
                new_salary = float(input("input new salary "))
                self.manager.update_employee_salary(name, new_salary)

            elif choice == "5":
                print("system closing")
                break

            else:
                print("wrong option, try again")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
