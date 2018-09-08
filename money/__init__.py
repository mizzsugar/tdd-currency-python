import abc


class Money(abc.ABC):
    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount and
            self.__class__ == money.__class__
        )

    @classmethod
    def dollar(cls, amount: int) -> 'Money':
        return Dollar(amount)

    @classmethod
    def franc(cls, amount: int) -> 'Money':
        return Franc(amount)

    @abc.abstractclassmethod
    def times(self, multiplier: int) -> 'Money':
        pass


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> 'Money':
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> 'Money':
        return Franc(self._amount * multiplier)
