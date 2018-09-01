class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount = amount
    
    def __eq__(self, dollar: 'Dollar') -> bool: 
        return self._amount == dollar._amount

    def times(self, multiplier: int) -> 'Dollar': 
        return Dollar(self._amount * multiplier)
