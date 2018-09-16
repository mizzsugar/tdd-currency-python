from typing import (
    Any,
    NamedTuple,
)
import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def reduce(self, bank: 'Bank') -> 'Money':
        pass

    def times(self, multiplier: int) -> 'Expression':
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

    def reduce(self, bank: 'Bank') -> 'Money':
        return self


class Bank:
    def __init__(self):
        self._rate_pairs = {}

    def reduce(self, expression: 'Expression', currency: str) -> 'Money':
        from_amount = expression.reduce(self)._amount
        from_currency = expression.reduce(self)._currency

        if from_currency == currency:
            return Money(
                from_amount,
                currency
            )
        return Money(
            from_amount * self._rate_pairs[from_currency, currency],
            currency
            )

    def add_rate(self, from_: str, to: str, rate: float) -> None:
        self._rate_pairs[Pair(from_, to)] = rate


class SumExpression(Expression):
    def __init__(self, augend: 'Expression', addend: 'Expression') -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: 'Bank') -> 'Money':
        au_currency = self.augend.reduce(bank)._currency
        ad_currency = self.addend.reduce(bank)._currency
        au_amount = self.augend.reduce(bank)._amount
        ad_amount = self.addend.reduce(bank)._amount

        if au_currency == ad_currency:
            return Money(
                au_amount + ad_amount,
                au_currency
                )
        reduced_amount = ad_amount / bank._rate_pairs[ad_currency, au_currency]
        return Money(
            au_amount + reduced_amount,
            au_currency
        )
        # reduce curreinces if those of augend and addend are different

    def plus(self, expression: 'Expression') -> 'SumExpression':
        return SumExpression(self, expression)

    def times(self, multiplier: int) -> 'SumExpression':
        au_expression = self.augend.times(multiplier)
        ad_expression = self.addend.times(multiplier)
        return SumExpression(au_expression, ad_expression)


class Pair(NamedTuple):
    from_: str
    to: str
