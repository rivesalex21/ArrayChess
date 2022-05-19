
import numpy as np

INITIAL_BOARD = np.array([['R','H','B','Q','K','B','H','R'],
                        ['P','P','P','P','P','P','P','P',],
                        [' ',' ',' ',' ',' ',' ',' ',' ',],
                        [' ',' ',' ',' ',' ',' ',' ',' ',],
                        [' ',' ',' ',' ',' ',' ',' ',' ',],
                        [' ',' ',' ',' ',' ',' ',' ',' ',],
                        ['p','p','p','p','p','p','p','p',],
                        ['r','h','b','q','k','b','h','r']])

map_letter = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
map_number = {'8':0,'7':1,'6':2,'5':3,'4':4,'3':5,'2':6,'1':7}
pieces = ['p','P','r','R','h','H','b','B','q','Q','k','K']
BOARD = INITIAL_BOARD.copy()


def Move(start,finish,BOARD):
    is_legal = False
    currentSpot = (map_number[start[1]], map_letter[start[0]])
    newSpot = (map_number[finish[1]], map_letter[finish[0]])

    is_legal = legalMoves(currentSpot,newSpot)
    if is_legal == True:
        BOARD[newSpot] = BOARD[currentSpot]
        BOARD[currentSpot] = ' '
    return BOARD

def legalMoves(start,finish):
    piece = BOARD[start]
    if piece == 'p':
        return legalMovesPawnWhite(start,finish)
    if piece == 'P':
        return legalMovesPawnBlack(start,finish)
    if piece == 'r':
        return legalMovesRook(start,finish)

def legalMovesPawnWhite(current_spot,end_spot):
    move1 = (current_spot[0]-1,current_spot[1])
    move2 = (current_spot[0]-2,current_spot[1])
    if current_spot[0] == 6:
        return end_spot in [move1,move2]
    return end_spot in [move1]

def legalMovesPawnBlack(current_spot,end_spot):
    move1 = (current_spot[0]+1,current_spot[1])
    move2 = (current_spot[0]+2,current_spot[1])
    if current_spot[0] == 1:
        return end_spot in [move1,move2]
    return end_spot in [move1]

def legalMovesRook(current_spot,end_spot):
    anchor_horizontal = current_spot[0]
    anchor_vertical = current_spot[1]
    moveList = []
    for i in range(8):
        moveList.append((anchor_horizontal,i))
        moveList.append((i,anchor_vertical))
    moveList.remove(current_spot)
    return end_spot in moveList

txt = ''
count = 0
while txt != 'exit' and count < 10:
    txt = input('Select movement: ')
    txt2 = input('Select movement: ')
    Move(txt, txt2, BOARD)
    print(BOARD)