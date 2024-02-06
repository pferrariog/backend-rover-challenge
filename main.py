from enum import StrEnum


class Directions(StrEnum):
    """Set a character to each cardinal direction"""

    north = "N"
    east = "E"
    south = "S"
    west = "W"


class CommandNotFound(Exception):
    """Rover's command not found exception"""

    def __init__(self, *args: object) -> None:
        """Initialize custom exception class"""
        super().__init__(*args)


class Rover:
    """Creates an object to a launched rover"""

    def __init__(self, start_x: str, start_y: str, start_position: str) -> None:
        """Iniatilize the class instance"""
        self.x = int(start_x)
        self.y = int(start_y)
        self.position = start_position

    def move(self, move: str) -> None:
        """Move the rover or turn it's direction"""
        directions_list = list(Directions)
        current_index = directions_list.index(self.position)

        if "M" in move:
            if self.position == "N":
                self.y += 1
            if self.position == "S":
                self.y -= 1
            if self.position == "E":
                self.x += 1
            if self.position == "W":
                self.x -= 1
            return

        if "L" in move:
            # ensures that the index does not exceed the list limit, returning to 0 when it reaches the limit
            new_index = (current_index - 1) % len(directions_list)
        elif "R" in move:
            new_index = (current_index + 1) % len(directions_list)
        else:
            raise CommandNotFound("Command not found")

        self.position = directions_list[new_index]


def read_input(input: str) -> list:
    """Read input file and return as list"""
    with open("input.txt") as file:
        input = file.read()
    return input.split("\n")


def process_rovers(splitted_input: list, max_x: int, max_y: int) -> None:
    """Process each rover by its own move sequence"""
    rovers = split_into_pairs(splitted_input)

    for rover_start, moves in rovers:
        start_position = rover_start.split(" ")
        rover = Rover(*start_position)

        for move in moves:
            rover.move(move)

        if rover.x > max_x or rover.y > max_y:
            print("rover ran out of bounds")
            return

        print(f"{rover.x} {rover.y} {rover.position}")


def split_into_pairs(list: list) -> list:
    """Split rovers and moves into pairs"""
    return [(list[i], list[i + 1]) for i in range(0, len(list), 2)]


def main() -> None:
    """Process main function"""
    rover_list = read_input()
    max_x, max_y = rover_list[0].split(" ")
    rover_list.pop(0)  # pop chart size
    process_rovers(rover_list, int(max_x), int(max_y))


if __name__ == "__main__":
    main()
