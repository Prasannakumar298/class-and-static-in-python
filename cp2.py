''' create a class atm and check the pin user1234
define a function to with draw 2000/-, balance amount from
account 5999, if the amount is over the balance exit and check
the print for the accesssing the account

class ATM:
    def __init__(self, pin, balance=5999):
        self.correct_pin = "user1234"
        self.pin = pin
        self.balance = balance
    
    def verify_pin(self):
        if self.pin == self.correct_pin:
            print("PIN verified successfully.")
            return True
        else:
            print("Invalid PIN.")
            return False
    
    def withdraw(self, amount=2000):
        print(f"Attempting to withdraw {amount}/- from account.")
        if amount > self.balance:
            print("Insufficient balance! Transaction cancelled.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}/-")
            return True
    
    def access_account(self):
        if self.verify_pin():
            success = self.withdraw()
            if not success:
                print("Cannot process the withdrawal due to insufficient funds.")
        else:
            print("Access denied.")

# Example usage:
atm = ATM(pin="user1234")
atm.access_account()'''

class ATM:
    def __init__(s):
        s.balance=5000
        s.pin="1234"
    def process(s):
        user_pin= input("Enter your 4-digit pin: ")
        if user_pin==s.pin:
            amount=int(input("Enter amount to debit:"))
            if amount<=s.balance:
                s.balance-=amount
                print(f"{amount} debited. Remaining balance: {s.balance}")
            else:
                print("Insufficient balance!..Transaction cancalled")
        else:
            print("Invalid PIN!..")
atm=ATM()
atm.process()