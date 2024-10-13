# class Company:
#     class Employee:
#         print('First Employee class')
        

# class NonProfit:
#     class Employee:
#         print('Second Employee class')


class Company:
    class Employee:
        
        def __init__(self, name, position, company):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f'{self.name} is a {self.position}'
        
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
        
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company('Google')
company2 = Company('Facebook')

company1.add_employee('John Doe', 'Software Engineer')
company1.add_employee('Jane Doe', 'Product Manager')
company1.add_employee('ADIB', 'Software Engineer')

company2.add_employee('John Smith', 'Software Engineer')
company2.add_employee('Jane Smith', 'Product Manager')
company2.add_employee('ADIB', 'Software Engineer')


print(company1.list_employees())

for employee in company2.list_employees():
    print(employee)