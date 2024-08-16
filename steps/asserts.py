from typing import Any
import allure
import pytest
from helpers.asserts import get_assert_function


@allure.step("Сравниваю набор значений")
def assert_that(left_side: Any, operator: str, right_side: Any):
    """
    Сравнивает значения между собой
    Поддерживаются операторы: 'equals', 'contains'
    Поддерживаются также варианты с отрицанием: 'not equals', 'not contains', например
    :param left_side: левый операнд
    :param operator: оператор сравнения
    :param right_side: правый операнд
    """
    assert_function = get_assert_function(operator)
    assert_function(left_side, right_side)


@allure.step("Сравниваю несколько наборов значений")
def assert_many(list_of_equations: list):
    """
    Сравнивает между собой несколько наборов значений
    Поддерживаются операторы: 'equals', 'contains'.
    Поддерживаются также варианты с отрицанием: 'not equals', 'not contains', например
    :param list_of_equations: кортеж вида (левый операнд, оператор сравнения, правый операнд)
    """
    for equation in list_of_equations:
        assert len(equation) == 3
        left_side, operator, right_side = equation
        assert_that(left_side, operator, right_side)


@allure.step("Проверяю существование")
def assert_existance(operand: Any):
    """
    Проверяет, что операнд существует
    :param operand: что угодно
    """
    try:
        assert operand
    except AssertionError:
        pytest.fail(f"Условие не выполнено:\n{operand} is not None")
