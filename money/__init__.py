class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, money: 'Moeny') -> bool:
        return (
            self._amount == money._amount and
            self._currency == money._currency
        )

    @classmethod
    def dollar(cls, amount: int) -> 'Money':
        return Dollar(amount)

    @classmethod
    def franc(cls, amount: int) -> 'Money':
        return Franc(amount)

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, 'USD')


class Franc(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, 'CHF')
