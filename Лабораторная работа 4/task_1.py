class BankAccount:
    """
    Базовый класс для банковского счета.
    """

    def __init__(self, account_number: str, balance: float):
        """
        Инициализация банковского счета.

        :param account_number: Номер счета
        :param balance: Баланс на счете
        """
        self._account_number = account_number  # Номер счета является приватным, чтобы предотвратить прямой доступ
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет.

        :param amount: Сумма для пополнения
        :raise ValueError: Если сумма пополнения отрицательная
        """
        if amount < 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма превышает баланс
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount

    def __str__(self) -> str:
        return f"Банковский счет {self._account_number}: Баланс {self.balance:.2f} руб."

    def __repr__(self) -> str:
        return f"BankAccount('{self._account_number}', {self.balance})"


class SavingsAccount(BankAccount):
    """
    Дочерний класс для сберегательного счета.
    """

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        """
        Инициализация сберегательного счета.

        :param account_number: Номер счета
        :param balance: Баланс на счете
        :param interest_rate: Процентная ставка
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        """
        Начисление процентов на баланс счета.
        """
        self.balance += self.balance * self.interest_rate

    def withdraw(self, amount: float) -> None:
        """
        Переопределение метода снятия средств.
        В сберегательном счете может быть ограничение на частоту снятий.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма превышает баланс
        """
        print("Внимание: снятие с сберегательного счета может быть ограничено!")
        super().withdraw(amount)

    def __str__(self) -> str:
        return f"Сберегательный счет {self._account_number}: Баланс {self.balance:.2f} руб., Ставка {self.interest_rate * 100:.1f}%"

    def __repr__(self) -> str:
        return f"SavingsAccount('{self._account_number}', {self.balance}, {self.interest_rate})"


if __name__ == "__main__":
    # Тестовые примеры
    acc1 = BankAccount("123456", 1000)
    acc2 = SavingsAccount("654321", 5000, 0.05)

    print(acc1)
    acc1.deposit(500)
    print(acc1)
    acc1.withdraw(200)
    print(acc1)

    print(acc2)
    acc2.add_interest()
    print(acc2)
    acc2.withdraw(1000)
    print(acc2)
