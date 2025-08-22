from my_project import add, sub, multiply, divide

def calculator():
    print("Welcome to mini calculator")
    print("choose operation:") 
    print("1.add\n 2.sub\n 3.multiply\n 4.divide")

    while True:
        choice = input("Enter choice(1/2/3/4/5):")

        if choice ==  '5':
            print ("Exiting calculator")
            break

        try:
            a = int(input("Enter first number:"))
            b =int(input("Enter second number:"))
        except ValueError:
            print ("Invalid number input. Try Again")
            continue
        if choice == '1':
            print("Result:", add.add(a,b))

        elif choice == '2':
            print("Result:",sub.sub(a,b))

        elif choice == '3':
            print("Result:",multiply.multiply(a,b))

        elif choice == '4':
     
            try:
                result = divide.divide(a, b)
                print("Result:", result)
            
            except ValueError:
                print ("ZeroDivisionError")
                
        else:
            print("invalid choice")

if __name__ == "__main__":
        calculator()

    
    