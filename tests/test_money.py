import pytest

import money


class TestMoney:
    @pytest.fixture
    def five_dollar(self):
        return money.Money.dollar(5)

    def test_currency(self, five_dollar):
        assert "USD" == five_dollar.currency()
        assert "CHF" == money.Money.franc(1).currency()

    def test_multiplication(self, five_dollar):
        assert money.Money.dollar(10) == five_dollar.times(2)
        assert money.Money.dollar(15) == five_dollar.times(3)

    def test_equality(self, five_dollar):
        assert five_dollar == five_dollar
        assert money.Money.franc(5) != money.Money.franc(6)
        assert money.Money.franc(5) != five_dollar

    def test_simple_addition(self, five_dollar):
        reduced = money.Bank().reduce(five_dollar.plus(five_dollar))

        assert reduced == money.Money.dollar(10)

    def test_plus_returns_sum(self, five_dollar):
        sum_expression = five_dollar.plus(five_dollar)

        assert sum_expression.augend == five_dollar
        assert sum_expression.addend == five_dollar
