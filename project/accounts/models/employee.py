from .models      import *
class Employee(Profile):
    def __str__(self):
        return self.first_name