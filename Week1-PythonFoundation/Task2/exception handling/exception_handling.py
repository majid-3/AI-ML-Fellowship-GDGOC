# This program performs basic calculations and handles errors safely

def calculator():
    while True:
        print("\nCalculator Menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)

            elif choice == "2":
                print("Result:", num1 - num2)

            elif choice == "3":
                print("Result:", num1 * num2)

            elif choice == "4":
                try:
                    result = num1 / num2
                    print("Result:", result)
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")
                    if choice == "5":
                        print("Exiting calculator.")
                    break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Error: Please enter valid numbers.")

# Program starts here
calculator()
