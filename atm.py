
class ATM:
    def __init__(self, pin):
        self.correct_pin = "user1234"
        self.balance = 5999
        self.pin = pin

    def access_account(self):
        if self.pin != self.correct_pin:
            print("Invalid PIN. Access denied.")
            return
        print("PIN verified successfully.")
        amount = 2000
        if amount > self.balance:
            print("Insufficient balance! Transaction cancelled.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}/-")

# Usage:
atm = ATM("user1234")
atm.access_account()
