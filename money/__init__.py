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
        return Money(amount, 'USD')

    @classmethod
    def franc(cls, amount: int) -> 'Money':
        return Money(amount, 'CHF')

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, added: 'Money') -> 'Money':
        return Money(self._amount + added._amount, self._currency)


class Bank:
    def reduce(self, money: 'Money') -> 'Money':
        return money
