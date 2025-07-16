import math

class Calculator:
    def __init__(self):
        self.history = []
        self.memory = 0
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    
    def sin(self, a):
        return math.sin(a)
    
    def cos(self, a):
        return math.cos(a)
    
    def tan(self, a):
        return math.tan(a)
    
    def log(self, a, base=math.e):
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        if base == math.e:
            return math.log(a)
        return math.log(a, base)
    
    def factorial(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(n)
    
    def percentage(self, a, b):
        return (a / 100) * b
    
    def memory_store(self, value):
        self.memory = value
        return f"Memory stored: {value}"
    
    def memory_recall(self):
        return self.memory
    
    def memory_clear(self):
        self.memory = 0
        return "Memory cleared"
    
    def evaluate_expression(self, expression):
        expression = expression.replace(' ', '').lower()
        
        expression = expression.replace('sqrt(', 'math.sqrt(')
        expression = expression.replace('sin(', 'math.sin(')
        expression = expression.replace('cos(', 'math.cos(')
        expression = expression.replace('tan(', 'math.tan(')
        expression = expression.replace('log(', 'math.log(')
        expression = expression.replace('pi', 'math.pi')
        expression = expression.replace('e', 'math.e')
        expression = expression.replace('^', '**')
        
        valid_chars = set('0123456789+-*/.()mathsincotanlgpier ')
        if not all(c in valid_chars for c in expression.replace('math.', '')):
            raise ValueError("Invalid characters in expression")
        
        try:
            safe_dict = {
                "__builtins__": {},
                "math": math
            }
            result = eval(expression, safe_dict)
            return result
        except Exception as e:
            raise ValueError("Invalid expression: " + str(e))
    
    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 10:
            self.history.pop(0)
    
    def show_history(self):
        if not self.history:
            return "No calculations in history"
        return "\n".join(self.history)
    
    def clear_history(self):
        self.history = []
        return "History cleared"

def display_menu():
    print("\n" + "="*50)
    print("           CALCULATOR SIMULATOR")
    print("="*50)
    print("1. Basic Operations (+, -, *, /)")
    print("2. Advanced Operations (^, sqrt, sin, cos, tan, log)")
    print("3. Expression Evaluation")
    print("4. Memory Operations (MS, MR, MC)")
    print("5. View History")
    print("6. Clear History")
    print("7. Help")
    print("8. Exit")
    print("="*50)

def display_help():
    help_text = """
CALCULATOR HELP
===============

Basic Operations:
- Addition: 5 + 3
- Subtraction: 10 - 4
- Multiplication: 6 * 7
- Division: 15 / 3
- Power: 2 ^ 3 (or 2 ** 3)

Advanced Operations:
- Square Root: sqrt(16)
- Sine: sin(1.57) [radians]
- Cosine: cos(0)
- Tangent: tan(0.785)
- Logarithm: log(10) [natural log]
- Factorial: 5! (enter as factorial)

Expression Examples:
- 2 + 3 * 4
- sqrt(16) + 5
- sin(pi/2)
- log(e)
- (2 + 3) * (4 - 1)

Memory Operations:
- MS: Memory Store
- MR: Memory Recall
- MC: Memory Clear

Constants:
- pi: 3.14159...
- e: 2.71828...
"""
    print(help_text)

def main():
    calc = Calculator()
    
    print("Welcome to the Python Calculator Simulator!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        try:
            if choice == '1':
                print("\n--- Basic Operations ---")
                print("Enter expression (e.g., 5 + 3, 10 - 2, 6 * 4, 15 / 3)")
                expr = input("Expression: ").strip()
                result = calc.evaluate_expression(expr)
                print(f"Result: {result}")
                calc.add_to_history(expr, result)
                
            elif choice == '2':
                print("\n--- Advanced Operations ---")
                print("Available: sqrt(x), sin(x), cos(x), tan(x), log(x), x^y")
                print("Examples: sqrt(16), sin(1.57), 2^3")
                expr = input("Expression: ").strip()
                
                if expr.endswith('!'):
                    num = int(expr[:-1])
                    result = calc.factorial(num)
                    print(f"Result: {result}")
                    calc.add_to_history(f"{num}!", result)
                else:
                    result = calc.evaluate_expression(expr)
                    print(f"Result: {result}")
                    calc.add_to_history(expr, result)
                
            elif choice == '3':
                print("\n--- Expression Evaluation ---")
                print("Enter complex expressions (e.g., 2 + 3 * 4, sqrt(16) + sin(pi/2))")
                expr = input("Expression: ").strip()
                result = calc.evaluate_expression(expr)
                print(f"Result: {result}")
                calc.add_to_history(expr, result)
                
            elif choice == '4':
                print("\n--- Memory Operations ---")
                print("MS: Memory Store | MR: Memory Recall | MC: Memory Clear")
                mem_op = input("Enter operation (MS/MR/MC): ").strip().upper()
                
                if mem_op == 'MS':
                    value = float(input("Enter value to store: "))
                    print(calc.memory_store(value))
                elif mem_op == 'MR':
                    print(f"Memory value: {calc.memory_recall()}")
                elif mem_op == 'MC':
                    print(calc.memory_clear())
                else:
                    print("Invalid memory operation")
                    
            elif choice == '5':
                print("\n--- Calculation History ---")
                print(calc.show_history())
                
            elif choice == '6':
                print(calc.clear_history())
                
            elif choice == '7':
                display_help()
                
            elif choice == '8':
                print("Thank you for using the Calculator Simulator!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1-8.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
