import money


class TestMoney:

    def test_multiplication(self):
        five = money.Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount

    def test_equality(self):
        assert money.Dollar(5) == money.Dollar(5)
