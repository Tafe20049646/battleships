from Log import Log
from ships.AircraftCarrier import AircraftCarrier
from ships.Battleship import Battleship
from ships.Submarine import Submarine
from ships.Cruiser import Cruiser
from ships.Destroyer import Destroyer
from ships.PatrolBoat import PatrolBoat


class Board:
    position = {}
    column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    row = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ships = []
    HORIZONTAL = 'H'
    VERTICAL = 'V'
    alive_ship = 10

    current_ship_number = 10

    def __init__(self):
        Log.info(' board init')

        self.ships.append(AircraftCarrier())
        self.ships.append(Battleship())
        self.ships.append(Cruiser())
        for x in range(3):
            self.ships.append(Submarine())

        for x in range(2):
            self.ships.append(Destroyer())
            self.ships.append(PatrolBoat())

        Log.info('ships length:' + str(len(self.ships)))

        self.init_grid()
        self.print_board()
        self.set_up_ship()

    def init_grid(self):
        for x in range(10):
            for j in range(10):
                self.position.setdefault(self.column[x] + str(j), '')

    # print the board
    def print_board(self):
        print('-------------------------------------------')
        print(f'  |{self.column[0].center(3)}|{self.column[1].center(3)}|{self.column[2].center(3)}|'
              f'{self.column[3].center(3)}|{self.column[4].center(3)}|{self.column[5].center(3)}|'
              f'{self.column[6].center(3)}|{self.column[7].center(3)}|{self.column[8].center(3)}|'
              f'{self.column[9].center(3)}|')

        for x in range(10):
            print('-------------------------------------------')
            print(f'{str(x)} |', end="")
            for y in range(10):
                row_position = self.column[y] + str(x)
                print(f'{self.position[row_position].center(3)}|', end="")
            print('')
        print('-------------------------------------------')

    # set up the ship position
    def set_up_ship(self):
        rest_ships = len(self.ships)
        for ship in self.ships:

            print(f'ships:{rest_ships}/{len(self.ships)}')
            rest_ships = rest_ships - 1
            print(f'The ship shapes  are {ship.shape}')
            orientation = self.set_orientation(ship)
            self.locate_ship(orientation, ship)
            self.print_board()

    # set the each orientation for each ships
    def set_orientation(self, ship):
        while True:
            print(f'set up {ship.name}')
            orientation = input('Entry the orientation H(Horizontal)/V(Vertical):').upper()
            if orientation is None:
                print('It is not a valid input.')
                continue
            if orientation == self.HORIZONTAL or orientation == self.VERTICAL:
                return orientation
            else:
                print('It is not a valid input.')
                return self.set_orientation(ship)

    # set the location from A0...A9 to J9
    def locate_ship(self, orientation, ship):
        while True:

            location = input('Please input the location from A0..A9 to J9:').upper()
            if location not in self.position:
                continue
            available_to_set_up = False
            if orientation == self.VERTICAL:
                available_to_set_up = self.vertical(location, ship)
            elif orientation == self.HORIZONTAL:
                available_to_set_up = self.horizontal(location, ship)
            if available_to_set_up is False:
                continue
            else:
                break

    def horizontal(self, location, ship):
        if self.is_location_in_position(location) is False:
            return False
        split = list(location)
        Log.info(f'index:{self.column.index(split[0])}')
        start_column = self.column.index(split[0])
        start_row = self.row.index(split[1])

        if (start_column + ship.shape) - 1 > len(self.column):
            print('The shape is over the grid, set up again please.')
            return False

        position_available = self.is_position_available(start_column, start_row, ship, self.HORIZONTAL)
        if position_available == True:
            self.input_ship(start_column, start_row, ship, self.HORIZONTAL)
        else:
            return False
        # for x in ship.shape:

    def vertical(self, location, ship):
        if self.is_location_in_position(location) is False:
            return False
        split = list(location)
        Log.info(f'index:{self.column.index(split[0])}')
        start_column = self.column.index(split[0])
        start_row = self.row.index(split[1])

        if (start_row + ship.shape) - 1 > len(self.row):
            print('*The shape is over the grid, set up again please.')
            return False

        position_available = self.is_position_available(start_column, start_row, ship, self.VERTICAL)
        if position_available == True:
            self.input_ship(start_column, start_row, ship, self.VERTICAL)
        else:
            print('*The shape is over the grid, set up again please.')
            return False

    def is_location_in_position(self, location):
        if location not in self.position:
            Log.info(f'position:{location} return')
            return False

    def split_location(self, location):
        return location.split()

    def is_position_available(self, start_column, start_row, ship, orientation):
        is_available = True

        for x in range(ship.shape):
            grid_column = self.column[start_column]
            grid_row = self.row[start_row]
            print(f'column:{grid_column}  row:{grid_row}')

            if self.position[grid_column + grid_row] != '':
                is_available = False
                continue
            if orientation == self.HORIZONTAL:
                start_column += 1
            elif orientation == self.VERTICAL:
                start_row += 1

        return is_available

    def input_ship(self, start_column, start_row, ship, orientation):
        ship_location = []
        for x in range(ship.shape):
            grid_column = self.column[start_column]
            grid_row = self.row[start_row]

            if self.position[grid_column + grid_row] != '':
                is_available = False
                continue
            self.position[grid_column + grid_row] = 'O'
            ship_location.append(grid_column + grid_row)
            if orientation == self.HORIZONTAL:
                start_column += 1
            elif orientation == self.VERTICAL:
                start_row += 1
        ship.set_position(ship_location)

    def hit(self):
        while True:
            location = input('Please input the location from A0..A9 to J9 to hit ship:').upper()
            if location not in self.position:
                print('* The input is invalid, input the location again please.')
                continue
            print('Boom!')
            if self.position[location] == '':
                print('Splash')
                self.position[location] = '*'
            elif self.position[location] == '*':
                print('Splash')
            elif self.position[location] == 'O':
                for ship in self.ships:
                    if ship.status:
                        if location in ship.position:
                            print(f'You sunk my {ship.name}')
                            ship.status = False
                            self.hit_the_ship(ship)
                            self.alive_ship = self.alive_ship - 1

            print(f'ships:{self.alive_ship}/{len(self.ships)}')
            self.print_board()
            break

    def hit_the_ship(self, ship):
        for position in ship.position:
            self.position[position] = 'X'
