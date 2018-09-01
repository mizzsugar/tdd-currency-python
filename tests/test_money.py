import money


class TestMoney:

    def test_multiplication(self):
        five = money.Dollar(5)
        five.times(2)
        assert 10 == five.amount
