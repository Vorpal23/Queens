    """This is my solution to the N-Queens Problem. it can currently 
        solve N-14 given enough computation time and some good luck.
        The algorithm constrains where a queen can go and tries to place
        queens in random valid spots until N queens are placed
    """
import os
import numpy as np
import funcQueens as q
import random

def main():
    n = 9
    chess_board = [[0 for i in range(n)] for i in range (n)]
    ix,iy=0,0
    qc=q.queen_count(chess_board)
    boards_found = 0
    solutions = []
    attempts = 0
    while True:
        attempts +=1
        chess_board = [[0 for i in range(n)] for i in range (n)]
        #chess_board =q.place_queen(ix,iy,chess_board)
        chess_board =q.place_queen(q.random_spot(chess_board),q.random_spot(chess_board),chess_board)
        
        for x in range(len(chess_board)):
            for y in range(len(chess_board[0])):
               #chess_board = q.place_if_valid(x,y,chess_board)
               chess_board = q.place_if_valid(q.random_spot(chess_board),q.random_spot(chess_board),chess_board)
    
        qc=q.queen_count(chess_board)
        if qc>=n:

            #print(q.queen_count(chess_board))
            #print(q.find_queen(chess_board))
            if q.find_queen(chess_board) not in solutions:
                """
                for x in chess_board:
                    print(x)
                """
                print(f'Found unique solution #{len(solutions)} on attempt: {attempts}')
                solutions.append(q.find_queen(chess_board))
                print(q.find_queen(chess_board))
                boards_found +=1
                attempts = 0
            else:
                print(f'Solution duplicate found on attempt: {attempts} solutions found: {len(solutions)}')
                
        if attempts>(len(solutions)+n)*100:
            print("ran out of attempts")
            break
        '''
        ix+=1
        if ix >=len(chess_board[0]):
            ix =0 
            iy+=1
        if iy>=len(chess_board):break        
        
        
        
        '''
    print(f'Found:{len(solutions)} solutions')
        

  

    
if __name__ == '__main__':
    main()
    
