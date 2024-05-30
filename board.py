import chess
# import pygame
# import requests
# import rembg
# from io import BytesIO
 
board=chess.Board()
while True:
    print(board)

    board.legal_moves
    move = input("enter move : ")

    board.push_san(move)

    print(board)
