class Bank:
    bank_name = "SBI"

    def __init__(self, name, age, balance):
        self.user_name = name
        self.age = age
        self.user_balance = balance

    def get_info(self):
        print(f'Bank: {self.bank_name}, User name: {self.user_name}, User Balance: {self.user_balance}')

b = Bank('Praveen', 22, 55000)
print(Bank.bank_name)
print(b.bank_name)
b.get_info()