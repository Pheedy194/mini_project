mini_project
mini_calculator
README.md


 Mini Calculator Package

A simple Python mini calculator project that demonstrates:
- Custom modules and packages
- Usage of __name__ == __main__
- Importing and organizing code
- Running the project in both terminal and Jupyter Notebook



 Project Structure

mini_calculator
│
├── operations/
│   ├── init.py
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   └── divide.py
│
└── main.py



Each math operation (add, subtract, multiply, divide) is in its own module.
 The operations folder is a package (because of __init__.py).
 main.py is the entry point that runs the calculator.

How to Run

 1. Clone the Repository

git clone https://github.com/Pheedy194/mini-calculator.git
cd mini-calculator


 2. Run in Terminal
 3. python main.py
 3. Run in Jupyter Notebook

Open a new notebook inside the project folder and import your package:

python
from operations import add, subtract, multiply, divide

print(add(5, 3))        # ➝ 8
print(subtract(10, 4))  # ➝ 6
print(multiply(7, 6))   # ➝ 42
print(divide(8, 2))     # ➝ 4.0



 Features

 Addition, Subtraction, Multiplication, Division
 Handles division by zero
 Modularized for easy maintenance and extension


 Example Run

 Mini Calculator 
Select operation: +, -, *, /
Enter operation: *
Enter first number: 6
Enter second number: 7
Result: 42







