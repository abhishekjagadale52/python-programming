def register_user():
    try:
        # Taking input from the user
        age = int(input("Enter your age for registration: "))

        # Checking if the age is within a valid range
        if age < 0 or age > 120:
            # Raising a ValueError if age is unrealistic
            raise ValueError("Age must be between 0 and 120.")
        
        print(f"Registration successful! Your age is: {age}")

    except ValueError as e:
        # This block catches both non-integer inputs and our custom range error
        print(f"Invalid Input: {e}")
    except Exception as e:
        # Catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the function
register_user()
