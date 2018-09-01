class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, dollar: 'Dollar') -> bool:
        return self._amount == dollar._amount

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)


class Franc:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, franc: 'Franc') -> bool:
        return self._amount == franc._amount

    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)
