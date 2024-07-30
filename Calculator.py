def display_menu():
    print("\n CALCULATOR!")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. EXIT")

def get_numbers():
    while True:

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2

        except ValueError:
            print("Oops! Please Try Aagin. :( ")

def calculation(choice, num1, num2):
    if choice == "1":
        result = num1 + num2
        operation = "+"
        
    elif choice == "2":
        result = num1 - num2
        operation = "-"

    elif choice == "3":
        result = num1 * num2
        operation = "*"

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            operation = "/"
        else:
             print("Division by zero is not allowed :( ")
             print("Please Try Aagin.")
             return None

    else:
        print("Something Is WRONG. Please Try Again.")
        return None

    return result, operation

def main():
    print("Hello!! This is a simple calculator, let's do some calculations together...")

    while True:

        display_menu()
        choice = input("What's your choice? (1/2/3/4/5): ")

        if choice == "5":
            print("GOODBYE!")
            break

        num1, num2 = get_numbers()

        result = calculation(choice, num1, num2)

        if result:
            print(f"\nHere's your result: {num1} {result[1]} {num2} = {result[0]}")
            print("Let's do another calculation!!")

main()
        
        

