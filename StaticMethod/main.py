class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_details(self): # its an instance method
        return f'{self.name} is a {self.position}'
    
    @staticmethod # statis method is not for to access data, it can be used as a utility function
    def is_validposition(position):
        valid_positions = ['Software Engineer', 'Product Manager', 'QA']
        return position in valid_positions # return True or False
    

print(Employee.is_validposition('Software Engineer')) # True
print(Employee.is_validposition('Data Scientist')) # False