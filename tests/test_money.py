import pytest

import money


class TestMoney:
    @pytest.fixture
    def five_dollar(self):
        return money.Money.dollar(5)

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
        reduced = money.Bank().reduce(five.plus(five))

        assert reduced == money.Money.dollar(10)

    def test_plus_returns_sum(self, five_dollar):
        sum_expression = five_dollar.plus(five_dollar)

        assert sum_expression.augend == five_dollar
        assert sum_expression.addend == five_dollar
