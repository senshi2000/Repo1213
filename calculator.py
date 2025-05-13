class Calculator:
    def __init__(self):
        self.add_result = 0
        self.sub_result = 0
        self.mul_result = 0
        self.div_result = 0
    
    def add(self, a, b):
        self.add_result = int(a + b)
        return self.add_result
    
    def subtract(self, a, b):
        self.sub_result = int(a - b)
        return self.sub_result
    
    def multiply(self, a, b):
        self.mul_result = int(a * b)
        return self.mul_result
    
    def divide(self, a, b):
        if b == 0:
            self.div_result = "Error: Division by zero"
            return self.div_result
        self.div_result = int(a // b)
        return self.div_result

    def get_add_result(self):
        return self.add_result

    def get_subtract_result(self):
        return self.sub_result

    def get_multiply_result(self):
        return self.mul_result

    def get_divide_result(self):
        return self.div_result
    
    def get_results(self):
        return {
            '足し算': self.add_result,
            '引き算': self.sub_result,
            '掛け算': self.mul_result,
            '割り算': self.div_result
        }
