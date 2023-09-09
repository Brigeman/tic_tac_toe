# Создаем игровое поле 3 на 3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отображения игрового поля
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Функция для проверки выигрыша
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Основной игровой цикл
current_player = 'X'
while True:
    display_board(board)
    row = int(input(f"Игрок {current_player}, введите номер строки (0, 1, 2): "))
    col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1, 2): "))

    if board[row][col] == ' ':
        board[row][col] = current_player
        if check_win(board, current_player):
            display_board(board)
            print(f"Игрок {current_player} выиграл!")
            break
        elif all([cell != ' ' for row in board for cell in row]):
            display_board(board)
            print("Ничья!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Эта ячейка уже занята. Попробуйте еще раз.")






