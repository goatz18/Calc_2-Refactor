"""Testing the Calculator"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction


@pytest.fixture(name="clear_history")
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def setup_addition_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)


@pytest.fixture
def setup_subtraction_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    subtraction = Subtraction(values)
    Calculations.add_calculation(subtraction)


def test_add_calculation_to_history(clear_history, setup_addition_calculation_fixture,
                                    setup_subtraction_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 2.0


def test_clear_calculation_history(clear_history, setup_addition_calculation_fixture,
                                   setup_subtraction_calculation_fixture):
    """ test_clear_calculation_history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 2.0
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True


def test_get_calculation(clear_history, setup_addition_calculation_fixture,
                         setup_subtraction_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(1).get_result() == -3.0


def test_get_calculation_last(clear_history, setup_addition_calculation_fixture,
                              setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation().get_result() == -3.0


def test_get_calculation_first(clear_history, setup_addition_calculation_fixture,
                               setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 3.0


def test_history_count(clear_history, setup_addition_calculation_fixture,
                       setup_subtraction_calculation_fixture):
    """Testing getting the history count"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 2.0


def test_get_calc_last_result_object(clear_history, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation(), Addition)
