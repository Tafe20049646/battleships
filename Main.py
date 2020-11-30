from Board import Board

if __name__ == '__main__':
    board = Board()

    while True:
        board.hit()
        if board.alive_ship == 0:
            break


