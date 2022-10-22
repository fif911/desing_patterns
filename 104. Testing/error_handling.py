import pytest


class CalculatorError(Exception):
    additional_data = "Our static data"


class Calculator:
    def add(self, first, second):
        try:
            res = first + second
        except TypeError as e:
            raise CalculatorError(f"You know, here is {e.__class__.__name__}")
        else:
            return res


class TestCalculator:
    def test_add_success(self):
        c = Calculator()

        assert c.add(1, 3) == 4

    def test_add_wierd(self):
        c = Calculator()

        with pytest.raises(CalculatorError):
            res = c.add("two", 3)

    def test_add_wierd_with_contex_analysis(self):
        c = Calculator()
        with pytest.raises(CalculatorError) as context:
            res = c.add("two", 3)

        assert context.typename == 'CalculatorError'
        assert str(context.value) == 'You know, here is TypeError'
        assert context.value.additional_data == "Our static data"
