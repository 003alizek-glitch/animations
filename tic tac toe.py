import copy
from tkinter import *

# Игроки
FirstPlayer = "X"
SecondPlayer = "O"

# Основное окно
window = Tk()
window.title("Tic Tac Toe")

# Глобальные переменные
game_btns = []
spaces = 9
current_player = FirstPlayer


# Проверка свободных клеток
def check_spaces():
    global spaces
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1
    return spaces != 0


# Получить противника
def get_enemy(player):
    return "O" if player == "X" else "X"


# Проверка победы
def check_winner(board, player):
    # Проверка строк
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Проверка колонок
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    # Диагонали
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Минимакс
def minimax(board, player, alpha, beta):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if not any(" " in row for row in board):
        return 0

    if player == "O":  # AI
        best_val = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    val = minimax(board, "X", alpha, beta)
                    board[i][j] = " "
                    best_val = max(best_val, val)
                    alpha = max(alpha, best_val)
                    if beta <= alpha:
                        break
        return best_val
    else:  # Игрок
        best_val = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    val = minimax(board, "O", alpha, beta)
                    board[i][j] = " "
                    best_val = min(best_val, val)
                    beta = min(beta, best_val)
                    if beta <= alpha:
                        break
        return best_val


# Ход AI
def ai_move():
    global current_player
    board_copy = [[game_btns[i][j]['text'] for j in range(3)] for i in range(3)]

    best_outcome = -1000
    best_move = None

    for i in range(3):
        for j in range(3):
            if board_copy[i][j] == " ":
                board_copy[i][j] = "O"
                val = minimax(board_copy, "X", -1000, 1000)
                board_copy[i][j] = " "
                if val > best_outcome:
                    best_outcome = val
                    best_move = (i, j)

    if best_move:
        game_btns[best_move[0]][best_move[1]]['text'] = "O"
        current_player = "X"
        label.config(text=FirstPlayer + " turn")


# Обработка клика
def clicked(row, col):
    global current_player
    if game_btns[row][col]['text'] == "" and current_player == "X":
        game_btns[row][col]['text'] = "X"
        if check_winner([[game_btns[i][j]['text'] for j in range(3)] for i in range(3)], "X"):
            label.config(text="Player X Wins!")
            return
        current_player = "O"
        label.config(text="O turn")
        window.after(500, ai_move)  # Задержка перед ходом AI


# Новая игра
def start_new_game():
    global spaces, current_player
    spaces = 9
    current_player = FirstPlayer
    for row in range(3):
        for col in range(3):
            game_btns[row][col]['text'] = ""
    label.config(text=FirstPlayer + " turn")


# Кнопка рестарт
restart_btn = Button(text="Restart", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side="top")

# Надпись чей ход
label = Label(text=(FirstPlayer + " turn"), font=('consolas', 30))
label.pack(side="top")

# Игровые кнопки
btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    row_buttons = []
    for col in range(3):
        btn = Button(btns_frame, text=" ", font=('consolas', 20), width=8, height=4,
                     command=lambda r=row, c=col: clicked(r, c))
        btn.grid(row=row, column=col)
        row_buttons.append(btn)
    game_btns.append(row_buttons)

window.mainloop()
