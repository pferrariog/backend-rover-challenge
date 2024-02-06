from main import Rover
from pytest import fixture


@fixture
def rover():
    return Rover("5", "2", "N")
