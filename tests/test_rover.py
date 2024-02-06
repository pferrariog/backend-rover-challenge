from main import CommandNotFound
from pytest import raises


def test_raise_exception_with_not_found_command(rover):
    with raises(CommandNotFound):
        rover.move("S")


def test_exception_should_return_message(rover):
    try:
        rover.move("S")
    except CommandNotFound as e:
        assert str(e) == "Command not found"


def test_turn_directions(rover):
    rover.move("R")

    assert rover.position == "E"

    rover.move("L")
    rover.move("L")

    assert rover.position == "W"

    rover.move("L")

    assert rover.position == "S"
