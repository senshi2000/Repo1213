class Calculator:
    def add(self, a, b):
        return int(a + b)
    
    def subtract(self, a, b):
        return int(a - b)
    
    def multiply(self, a, b):
        return int(a * b)
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return int(a // b)
