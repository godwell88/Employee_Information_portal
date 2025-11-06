class Employee:
    def __init__(self, emp_id, name, dept, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.role = role
        self.salary = salary

    def show(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Dept: {self.dept} | Role: {self.role} | Salary: ₹{self.salary}")


class EmployeePortal:
    def __init__(self):
        self.employees = []
        self.next_id = 1

    def add_employee(self):
        name = input("Enter name: ")
        dept = input("Enter department: ")
        role = input("Enter role: ")
        salary = float(input("Enter salary: "))
        emp = Employee(self.next_id, name, dept, role, salary)
        self.employees.append(emp)
        self.next_id += 1
        print("Employee added successfully!\n")

    def show_all(self):
        if not self.employees:
            print("No employees found.\n")
            return
        print("\n--- Employee List ---")
        for e in self.employees:
            e.show()
        print()

    def search_employee(self):
        choice = input("Search by (1) ID or (2) Name: ")
        if choice == "1":
            emp_id = int(input("Enter Employee ID: "))
            for e in self.employees:
                if e.emp_id == emp_id:
                    e.show()
                    break
            else:
                print("Employee not found.\n")
        elif choice == "2":
            name = input("Enter name: ").lower()
            found = False
            for e in self.employees:
                if name in e.name.lower():
                    e.show()
                    found = True
            if not found:
                print("Employee not found.\n")
        else:
            print("Invalid choice.\n")

    def update_employee(self):
        emp_id = int(input("Enter Employee ID to update: "))
        for e in self.employees:
            if e.emp_id == emp_id:
                print("Leave blank to keep current value.")
                name = input(f"Name ({e.name}): ") or e.name
                dept = input(f"Department ({e.dept}): ") or e.dept
                role = input(f"Role ({e.role}): ") or e.role
                salary_input = input(f"Salary ({e.salary}): ")
                salary = float(salary_input) if salary_input else e.salary
                e.name, e.dept, e.role, e.salary = name, dept, role, salary
                print("Employee updated successfully!\n")
                return
        print("Employee not found.\n")

    def delete_employee(self):
        emp_id = int(input("Enter Employee ID to delete: "))
        for e in self.employees:
            if e.emp_id == emp_id:
                self.employees.remove(e)
                print(" Employee deleted.\n")
                return
        print("Employee not found.\n")


def main():
    portal = EmployeePortal()
    while True:
        print("=== Employee Information Portal ===")
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            portal.add_employee()
        elif choice == "2":
            portal.show_all()
        elif choice == "3":
            portal.search_employee()
        elif choice == "4":
            portal.update_employee()
        elif choice == "5":
            portal.delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
