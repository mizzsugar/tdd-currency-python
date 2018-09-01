class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount
    
    def __eq__(self, dollar: 'Dollar') -> bool: 
        return self.amount == dollar.amount

    def times(self, multiplier: int) -> 'Dollar': 
        return Dollar(self.amount * multiplier)
