class User:
    """A basic template for a User"""
    def __init__(self, first_name, last_name):
        """Initialize the user with a first and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """prints basic information"""
        print(f"{self.first_name} {self.last_name}")
    
    def greet_user(self):
        """Greets the user by their first name"""
        print(f"Hello {self.first_name}. I hope this day finds you well.")
    
    def increment_login_attemtpts(self):
        """Increments the users login attempt count by 1"""
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        """Resets the user login attempt count to 0"""
        self.login_attempts = 0
    
user1 = User('Chase', 'Wilson')

user1.increment_login_attemtpts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
    
    
