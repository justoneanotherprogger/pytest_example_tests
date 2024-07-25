import pytest


def get_assert_function(operator):
    if operator == 'equals':
        return assert_equals
    elif operator == 'not equals':
        return assert_not_equals
    elif operator == 'contains':
        return assert_contains
    elif operator == 'not contains':
        return assert_not_contains
    else:
        pytest.fail('Некорректный оператор сравнения')


def assert_equals(left_side, right_side):
    try:
        assert left_side == right_side
    except AssertionError:
        pytest.fail(f"Условие не выполняется:\n\"{left_side}\" == \"{right_side}\"")


def assert_not_equals(left_side, right_side):
    try:
        assert left_side != right_side
    except AssertionError:
        pytest.fail(f"Условие не выполняется:\n\"{left_side}\" != \"{right_side}\"")


def assert_contains(left_side, right_side):
    try:
        assert right_side in left_side
    except AssertionError:
        pytest.fail(f"Условие не выполняется:\n\"{left_side}\" contains \"{right_side}\"")


def assert_not_contains(left_side, right_side):
    try:
        assert not (right_side in left_side)
    except AssertionError:
        pytest.fail(f"Условие не выполняется:\n\"{left_side}\" not contains \"{right_side}\"")
