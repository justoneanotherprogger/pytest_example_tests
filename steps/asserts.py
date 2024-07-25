from typing import Any
import allure
import pytest
from helpers.asserts import get_assert_function


@allure.step("Сравниваю набор значений")
def assert_that(left_side: Any, operator: str, right_side: Any):
    """
    Сравнивает значения между собой
    :param left_side: Левый операнд
    :param operator: Оператор сравнения. Поддерживаются операторы: equals, contains
    :param right_side: Правый операнд
    """
    assert_function = get_assert_function(operator)
    assert_function(left_side, right_side)


@allure.step("Сравниваю несколько наборов значений")
def assert_many(list_of_equations: list):
    for equation in list_of_equations:
        assert len(equation) == 3
        left_side, operator, right_side = equation
        assert_that(left_side, operator, right_side)


@allure.step("Проверяю существование")
def assert_existance(operand: Any):
    try:
        assert operand
    except AssertionError:
        pytest.fail(f"Условие не выполнено:\n{operand} is not None")
