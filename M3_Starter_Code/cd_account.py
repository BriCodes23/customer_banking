"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account( balance, interest_rate)
    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/0)
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
class cd_account:

    def _init_(self, balance):
        self.balance = balance

    def set_balance(self, updated_balance):
        self.balance = updated_balance

        Account = cd_account(1000)
        updated_balance = 1500
        Account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
cd = cd_account(balance, interest_rate)

cd.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return updated_balance, interest_rate
