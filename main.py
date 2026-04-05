from calculator import calculate

history = []

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Please enter a valid number!")

def show_history():
    print("\n" + "=" * 35)
    print("   📜  Calculation History")
    print("=" * 35)
    if not history:
        print("  No calculations yet!")
    else:
        for i, record in enumerate(history, 1):
            print(f"  {i}. {record}")
    print("=" * 35)

def main():
    print("=" * 35)
    print("   🧮  Simple Python Calculator")
    print("=" * 35)

    while True:
        print("\nOperators:  +  |  -  |  *  |  /  |  ^  |  sqrt")
        print("Commands:   'history' to view | 'quit' to exit\n")

        num1 = get_number("Enter first number : ")

        operator = input("Enter operator     : ").strip().lower()

        if operator == 'quit':
            print("\n👋 Thanks for using the calculator!")
            break

        if operator == 'history':
            show_history()
            continue

        # sqrt only needs one number
        if operator == 'sqrt':
            result = calculate(num1, operator)
            entry = f"sqrt({num1}) = {result}"
        else:
            num2 = get_number("Enter second number: ")
            result = calculate(num1, operator, num2)
            entry = f"{num1} {operator} {num2} = {result}"

        print(f"\n✅  {entry}")
        print("-" * 35)

        # Save to history
        history.append(entry)

        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            show_history()
            print("\n👋 Thanks for using the calculator!")
            break

if __name__ == "__main__":
    main()20