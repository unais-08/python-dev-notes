class BankAccount:
    def __init__(self, name: str, acc_no: int, balance: float = 0.0):
        self._name = name
        self._acc_no = acc_no
        self._balance = balance

    def print_details(self) -> None:
        print(f"Account Holder: {self._name}")
        print(f"Account Number: {self._acc_no}")
        print(f"Account Balance: ${self._balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self._balance < amount:
            print("Insufficient funds!")
            return False
        self._balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")
        return True

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        print(f"${amount:.2f} deposited successfully.")
        return True


if __name__ == "__main__":
    account = BankAccount("xyz", 1234)
    account.deposit(2000)
    account.withdraw(100)
    account.print_details()
