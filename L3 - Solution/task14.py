from typing import List, Dict
from functools import reduce

def process_employee_data(employee_data: List[Dict[str, int]]):
    filtered_employee_data = list(filter(lambda x: 25 <= x['age'] <= 40, employee_data))
    sorted_employee_data = sorted(filtered_employee_data, key=lambda x: x['salary'])
    grouped_employee_data = {}
    for employee in sorted_employee_data:
        department = employee['department']
        if department not in grouped_employee_data:
            grouped_employee_data[department] = []
        grouped_employee_data[department].append(employee)
    avg_salary_per_department = {}
    for department, employees in grouped_employee_data.items():
        avg_salary = reduce(lambda x, y: x + y, [employee['salary'] for employee in employees]) / len(employees)
        avg_salary_per_department[department] = avg_salary
    return avg_salary_per_department

employee_data = [{'name': 'John Doe', 'age': 30, 'salary': 50000, 'department': 'IT'},
                 {'name': 'Jane Doe', 'age': 35, 'salary': 55000, 'department': 'HR'},
                 {'name': 'Jim Smith', 'age': 40, 'salary': 60000, 'department': 'IT'},
                 {'name': 'Amy Johnson', 'age': 32, 'salary': 53000, 'department': 'HR'},
                 {'name': 'Tom Brown', 'age': 38, 'salary': 57000, 'department': 'IT'}]

result = process_employee_data(employee_data)
print(result)

# Output: {'IT': 55000.0, 'HR': 54000.0}
