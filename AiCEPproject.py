# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:27:30 2024

@author: Abdullah
"""

board = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def print_board():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print()

def check_for_win(player):
    return ((board[1] == board[2] == board[3] == player) or 
        (board[4] == board[5] == board[6] == player) or
        (board[7] == board[8] == board[9] == player) or 
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or 
        (board[3] == board[6] == board[9] == player) or
        (board[1] == board[5] == board[9] == player) or 
        (board[3] == board[5] == board[7] == player))

def check_for_draw():
    return all(space != " " for space in board.values())

def minimax(board, is_maximizing):
    if check_for_win("o"):
        return 1
    if check_for_win("x"):
        return -1
    if check_for_draw():
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board, False)
                board[key] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board, True)
                board[key] = " "
                best_score = min(best_score, score)
        return best_score

def play_computer():
    best_score = -float('inf')
    best_move = None
    for key in board.keys(): #checking all empty positions
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board, False)
            board[key] = " "     #Backtracking
            if score > best_score:
                best_score = score
                best_move = key
    board[best_move] = "o"

def play_game():
    turn = "x"
    while True:
        print_board()
        
        if check_for_win("x"):
            print("Player X wins!")
            break
        if check_for_win("o"):
            print("AI wins!")
            break
        if check_for_draw():
            print("It's a draw!")
            break
        
        if turn == "x":
            move = int(input("Player X, enter your move (1-9): "))
            if board[move] == " ":
                board[move] = "x"
                turn = "o"
            else:
                print("Invalid move. Try again.")
        else:
            play_computer()
            turn = "x"

play_game()