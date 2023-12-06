import os

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(7)] for _ in range(7)]
        self.ships = [Ship(3), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]
        self.attempts = 0

    def place_ships(self):
        for ship in self.ships:
            while True:
                x, y = self.get_coordinates(f"Enter starting coordinates (row, column) for {ship.size}-unit ship: ")
                orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()

                if self.is_valid_placement(x, y, ship.size, orientation):
                    self.mark_ship(x, y, ship.size, orientation)
                    break
                else:
                    print("Invalid placement. Try again.")

    def get_coordinates(self, prompt):
        while True:
            try:
                x, y = map(int, input(prompt).split())
                if 1 <= x <= 7 and 1 <= y <= 7:
                    return x - 1, y - 1
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    def is_valid_placement(self, x, y, size, orientation):
        if orientation == 'H':
            return y + size <= 7 and all(self.board[x][i] == ' ' for i in range(y, y + size))
        elif orientation == 'V':
            return x + size <= 7 and all(self.board[i][y] == ' ' for i in range(x, x + size))
        return False

    def mark_ship(self, x, y, size, orientation):
        if orientation == 'H':
            for i in range(y, y + size):
                self.board[x][i] = 'O'
        elif orientation == 'V':
            for i in range(x, x + size):
                self.board[i][y] = 'O'

    def display_board(self, hide_ships=False):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("   A B C D E F G")
        print("  +-+-+-+-+-+-+-+")
        for i in range(7):
            print(f"{i+1} |", end=' ')
            for j in range(7):
                if not hide_ships and self.board[i][j] == 'O':
                    print('O', end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

def play_battleship():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! It's time to place your ships.")
    player.place_ships()

    input("Ships placed! Press Enter to start the battle.")

    while any(ship.hits < ship.size for ship in player.ships):
        player.display_board()
        x, y = player.get_coordinates("Enter coordinate for your shot (row, column): ")

        if player.board[x][y] == 'O':
            print("Hit!")
            player.board[x][y] = 'X'
            for ship in player.ships:
                if all(player.board[i][j] == 'X' for i in range(7) for j in range(7) if (i, j) in [(r, c) for r in range(7) for c in range(7)]):
                    ship.hits += 1
                    print(f"You sunk a {ship.size}-unit ship!")
        else:
            print("Miss!")

        player.attempts += 1
        input("Press Enter to continue.")

    print(f"Congratulations, {player.name}! You sank all the ships in {player.attempts} attempts.")

if __name__ == "__main__":
    play_battleship()                   
