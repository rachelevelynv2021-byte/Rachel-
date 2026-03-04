class Employee:
    def __init__(self, emp_id, personality, experience, trust, predictions):
        self.emp_id = emp_id
        self.personality = personality
        self.experience = experience
        self.trust = trust
        self.predictions = predictions

class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, personality, experience, trust, predictions):
        if emp_id not in self.employees:
            self.employees[emp_id] = Employee(emp_id, personality, experience, trust, predictions)
        else:
            print('Employee ID already exists.')

    def get_employee(self, emp_id):
        return self.employees.get(emp_id, 'Employee not found.')

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
        else:
            print('Employee ID not found.')

    def list_employees(self):
        return self.employees.values()