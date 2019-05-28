class Employee:
    """A class to model an employee."""
    def __init__(self, first, last, annual_salary):
        """Initializes the Emplyee class with a first and last name
        as well as an annual salary."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_increase = 5000):
        """Increments annual salary by 5,000 as a default."""
        self.annual_salary += salary_increase
    
test = Employee('Chase', 'Wilson', 117000)
   
    