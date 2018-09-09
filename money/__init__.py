from typing import (
    Any,
    NamedTuple,
)
import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def reduce(self) -> 'Money':
        pass


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Money):
            return False

        return (
            self._amount == other._amount and
            self._currency == other._currency
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

    def plus(self, addend: 'Money') -> 'SumExpression':
        return SumExpression(self, addend)

    def reduce(self) -> 'Money':
        return self


class Bank:
    def __init__(self):
        self._rate_pairs = {}

    def reduce(self, expression: 'Expression', currency: str) -> 'Money':
        if expression.reduce()._currency == "CHF" and currency == "USD":
            return Money.dollar(expression.reduce()._amount * self._rate_pairs["CHF", "USD"])
        elif expression.reduce()._currency == "USD" and currency == "CHF":
            return Money.franc(expression.reduce()._amount / self._rate_pairs["USD", "CHF"])
        return Money(expression.reduce()._amount, currency)

    def add_rate(self, from_: str, to: str, rate: int) -> 'Bank':
        self._rate_pairs[Pair(from_, to)] = rate

class SumExpression(Expression):
    def __init__(self, augend: 'Money', addend: 'Money') -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self) -> 'Money':
        return Money(
            self.augend._amount + self.addend._amount,
            self.augend._currency
        )


class Pair(NamedTuple):
    from_: str
    to: str
