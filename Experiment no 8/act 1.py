# Custom Exception for Insufficient Funds
class InsufficientBalanceError(Exception):
    def _init_(self, message="Error: Insufficient balance for this withdrawal."):
        self.message = message
        super()._init_(self.message)

def withdraw_money(account_balance, amount):
    try:
        print(f"Current Balance: ₹{account_balance}")
        print(f"Attempting to withdraw: ₹{amount}")
        
        # Check if withdrawal amount is greater than current balance
        if amount > account_balance:
            raise InsufficientBalanceError()
        
        # Deduct balance if sufficient
        account_balance -= amount
        print(f"Withdrawal Successful! Remaining Balance: ₹{account_balance}")
        
    except InsufficientBalanceError as e:
        print(e)
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
    finally:
        print("Transaction session ended.")

# Example Usage
withdraw_money(5000, 6000)
