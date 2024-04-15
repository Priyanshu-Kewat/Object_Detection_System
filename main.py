def print_board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def free_space(position):
    return board[position] == ' '

def insert_letter(letter, position):
    if free_space(position):
        board[position] = letter
        print_board(board)
        if check_draw():
            print("Its a tie")
            exit()
        if check_win():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def check_which_mark_won(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
    
def check_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 

def player_move():
    position = int(input("Enter a position for 'O': "))
    insert_letter(player, position)

def comp_move():
    best_score = float('-inf')
    best_move = None
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = alpha_beta_pruning(board, False, float('-inf'), float('inf'))
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    insert_letter(bot, best_move)

def alpha_beta_pruning(board, is_maximizing, alpha, beta):
    if check_which_mark_won(bot):
        return 1
    elif check_which_mark_won(player):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = alpha_beta_pruning(board, False, alpha, beta)
                board[key] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = alpha_beta_pruning(board, True, alpha, beta)
                board[key] = ' '
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score


if __name__ == "__main__":
    board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
    player = 'O'
    bot = 'X'

    while not check_win():
        comp_move()
        player_move()
