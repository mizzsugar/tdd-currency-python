import pytest

import money


class TestMoney:
    @pytest.fixture
    def five_dollar(self):
        return money.Money.dollar(5)

    @pytest.fixture
    def bank(self):
        bank = money.Bank()
        bank.add_rate("CHF", "USD", 2)
        return bank

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
        reduced = money.Bank().reduce(five_dollar.plus(five_dollar), "USD")

        assert reduced == money.Money.dollar(10)

    def test_plus_returns_sum(self, five_dollar):
        sum_expression = five_dollar.plus(five_dollar)

        assert sum_expression.augend == five_dollar
        assert sum_expression.addend == five_dollar

    def test_reduce_sum(self):
        sum_expression = money.SumExpression(
            money.Money.dollar(3), money.Money.dollar(4))
        reduced = money.Bank().reduce(sum_expression, "USD")
        assert reduced == money.Money.dollar(7)

    def test_reduce_to_different_currency(self):
        bank = money.Bank()
        bank.add_rate("CHF", "USD", 2)
        actual = bank.reduce(money.Money.franc(2), "USD")
        assert actual == money.Money.dollar(4)

    def test_mixed_addition(self, five_dollar):
        bank = money.Bank()
        bank.add_rate("CHF", "USD", 2)

        franc = money.Money.franc(10)
        actual = bank.reduce(five_dollar.plus(franc), "USD")
        assert actual == money.Money.dollar(10)

    def test_sum_plus_money(self, bank, five_dollar):
        franc = money.Money.franc(10)
        expression = money.SumExpression(five_dollar, franc).plus(five_dollar)
        assert bank.reduce(expression, "USD") == money.Money.dollar(15)
