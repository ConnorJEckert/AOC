from itertools import chain


def column(matrix, i):
    return [row[i] for row in matrix]

def check_win(board, numbers):
    numbers = set(numbers)
    for row in board:
        if (set(row).issubset(numbers)):
            return True
    for i in range(len(board[0])):
        if (set(column(board, i)).issubset(numbers)):
            return True
    return False
        
def calc_score(board, numbers):
    flat_board = list(chain.from_iterable(board))
    uncalled_nums = set(flat_board) - set(numbers)
    return sum(uncalled_nums)

def generate_boards(fp):
    boards = []
    while True:
        board = []
        for i in range(5):
            board.append([int(number) for number in fp.readline().split()])
        fp.readline().strip()
        if (board == [[],[],[],[],[]]):
            return boards
        boards.append(board)
    


def star1():
    with open("input.txt") as fp:
        pulls = [int(number) for number in fp.readline().split(',')]
        fp.readline()

        boards = generate_boards(fp)

        for i in range(len(pulls)):
            nums = pulls[:i+1]
            for board in boards:
                if (check_win(board, nums)):
                    print(calc_score(board, nums) * nums[-1])
                    return

def star2():
    with open("input.txt") as fp:
        pulls = [int(number) for number in fp.readline().split(',')]
        fp.readline()

        boards = generate_boards(fp)

        for i in range(len(pulls)):
            nums = pulls[:i+1]
            for board in boards:
                if (check_win(board, nums)):
                    if (len(boards)>1):
                        boards.remove(board)
                    else:
                        print(calc_score(board, nums) * nums[-1])
                        return

star2()