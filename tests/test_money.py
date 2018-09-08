import money


class TestMoney:

    def test_multiplication(self):
        five = money.Dollar(5)
        assert money.Dollar(10) == five.times(2)
        assert money.Dollar(15) == five.times(3)

    def test_equality(self):
        assert money.Dollar(5) == money.Dollar(5)
        assert money.Dollar(6) == money.Dollar(6)
        assert money.Franc(5) == money.Franc(5)
        assert money.Franc(5) != money.Franc(6)

    def test_franc_multiplication(self):
        five = money.Franc(5)
        assert money.Franc(10) == five.times(2)
        assert money.Franc(15) == five.times(3)
