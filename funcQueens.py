import numpy as np
import random
def random_spot(board):
    return random.randint(0,len(board)-1)
def place_queen(x,y,board):
    h,w = len(board),len(board[0])
    for i in range(h):
        for j in range(w):
            board[i][y]=1
            board[x][j]=1
            
            if x+i <h and y+i<w:board[x+i][y+i]=1
            if x-i>=0 and y-i>=0:board[x-i][y-i]=1
            if x+i<h and y-i>=0:board[x+i][y-i]=1
            if x-i>=0 and y+i<w:board[x-i][y+i]=1
            
    d = np.diag_indices(len(board))
    np.array(board)[d] = 1        
            
    
    '''
    board[x+1][y+1]
    board[x+2][y+2]
    board[x+3][y+3]
    
    
    '''

    board[x][y] = 8
    return board
def place_if_valid(x,y,board):
    return place_queen(x,y,board) if board[x][y]==0 else board
def queen_count(board):
    h,w,q= len(board),len(board[0]),0
    for x in range(h):
        for y in range(w):
            q+=1 if board[x][y] == 8 else 0
    return q
def find_queen(board):
    ranks = {
  0: "A",
  1: "B",
  2: 'C',
  3: "D",
  4: "E",
  5: 'F',
  6: "G",
  7: 'H',
  8: "I",
  9: "J",
  10: 'K',
  11: "L",
  12: "M",
  13: 'N',
  14: "O",
  15: 'P',
  
}
    h,w,q= len(board),len(board[0]),[]
    for x in range(h):
        for y in range(w):
            if board[x][y] == 8:
                 q.append((ranks[x],y+1))
        
    return q
            
    
