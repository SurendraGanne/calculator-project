from calculator import calculate

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Please enter a valid number!")

def main():
    print("=" * 35)
    print("   🧮  Simple Python Calculator")
    print("=" * 35)

    while True:
        print("\nOperators:  +  |  -  |  *  |  /")
        print("Type 'quit' to exit\n")

        num1 = get_number("Enter first number : ")
        
        operator = input("Enter operator     : ").strip()
        if operator.lower() == 'quit':
            break

        num2 = get_number("Enter second number: ")

        result = calculate(num1, operator, num2)

        print(f"\n✅  {num1} {operator} {num2} = {result}")
        print("-" * 35)

        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n👋 Thanks for using the calculator!")
            break

if __name__ == "__main__":
    main()