def split_bill():
    try:
        total_bill = float(input("Enter total bill amount: "))
        number_of_people = int(input("Enter number of people: "))

        # This line will trigger a ZeroDivisionError if people == 0
        amount_per_person = total_bill / number_of_people
        
        print(f"Each person should pay: {amount_per_person:.2f}")

    except ZeroDivisionError:
        # Specifically handles the case where the user enters 0
        print("Error: You cannot divide a bill among zero people.")
        
    except ValueError:
        # Handles cases where the user enters text instead of a number
        print("Error: Please enter a valid numerical value.")

# Run the function
split_bill()
