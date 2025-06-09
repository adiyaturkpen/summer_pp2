class bank_acc:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, c):
        self.balance += c
        print(f"Пополнено на {c}. Ваш баланс: {self.balance}")

    def withdraw(self, c):
        if c > self.balance:
            print("Недостаточно средств.")
        else:
            self.balance -= c
            print(f"Снято {c}. Ваш баланс: {self.balance}")

    def show(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance}")

acc = bank_acc("Adiya", 0)
acc.show()
for i in range(3):
    c = float(input("Введите сумму для пополнения: "))
    acc.deposit(c)

    c = float(input("Введите сумму для снятия: "))
    acc.withdraw(c)
acc.show()
