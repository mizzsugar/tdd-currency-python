import money


class TestMoney:
    def test_currency(self):
        assert "USD" == money.Money.dollar(1).currency()
        assert "CHF" == money.Money.franc(1).currency()

    def test_multiplication(self):
        five = money.Money.dollar(5)
        assert money.Money.dollar(10) == five.times(2)
        assert money.Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert money.Money.dollar(5) == money.Money.dollar(5)
        assert money.Money.franc(5) != money.Money.franc(6)
        assert money.Money.franc(5) != money.Money.dollar(5)

    def test_simple_addition(self):
        five = money.Money.dollar(5)
        assert five.plus(five) == money.Money.dollar(10)
