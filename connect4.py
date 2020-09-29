"""
    Project name : Connect 4 Project
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

picPlay = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

COL_COUNT = 7
ROW_COUNT = 6
OFFSET_VAL= 1
DEADZONE = 3
PIECE_P1 = "X"
PIECE_P2 = "O"

def drawBoard(field):
    x = 15
    y = 12
    col = int(x)
    row = int(y)
    for i in range(row):
        if (int(i) % 2 == 0):
            pracRow = int(i)/2
            for ci in range(col):
                if(int(ci)%2 == 0):
                    pracCol = int(ci)/2
                    if (ci != 14):
                        print(field[int(pracCol)][int(pracRow)],end ="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-"*14)

def inAte():
    picPlay = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

def validateWin(field,piece):
#       evaluate Horizontal
        for c in range(COL_COUNT-3):
            for r in range(ROW_COUNT):
                itm1 = field[c][r]
                itm2 = field[c+1][r]
                itm3 = field[c+2][r]
                itm4 = field[c+3][r]
                if itm1 == piece and itm2 == piece and itm3 == piece and itm4 == piece :
                    return True
#       evaluate Vertical
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT-OFFSET_VAL,DEADZONE-OFFSET_VAL,-1):
                itm1 = field[c][r]
                itm2 = field[c][r-1]
                itm3 = field[c][r-2]
                itm4 = field[c][r-3]
                if itm1 == piece and itm2 == piece and itm3 == piece and itm4 == piece :
                    return True
#       positive diag slope
        for c in range(COL_COUNT-DEADZONE):
            for r in range(ROW_COUNT-OFFSET_VAL,DEADZONE-OFFSET_VAL,-1):
                itm1 = field[c][r]
                itm2 = field[c+1][r-1]
                itm3 = field[c+2][r-2]
                itm4 = field[c+3][r-3]
                print(itm1,itm2,itm3,itm4)
                if itm1 == piece and itm2 == piece and itm3 == piece and itm4 == piece :
                    return True
#       negative diag slope
        for c in range(COL_COUNT-DEADZONE,DEADZONE-OFFSET_VAL,-1):
            for r in range(ROW_COUNT-OFFSET_VAL,DEADZONE-OFFSET_VAL,-1):
                itm1 = field[c][r]
                itm2 = field[c-1][r-1]
                itm3 = field[c-2][r-2]
                itm4 = field[c-3][r-3]
                if itm1 == piece and itm2 == piece and itm3 == piece and itm4 == piece :
                    return True

def playPiece(player,piece):
    i = ROW_COUNT-OFFSET_VAL
    while i >= 0:
        if picPlay[ColSelect][i] == " ":
            picPlay[ColSelect][i] = piece
            break
        else:
            i -= 1
            continue


Player = 1
GameOver = False
turn = 0
while not GameOver:
    drawBoard(picPlay)
    if turn == 0:
        print("Player No: ",Player)
        actSelect = int(input("Please enter the column to drop tile:(1-7) "))
        ColSelect = actSelect-OFFSET_VAL
        playPiece(Player,PIECE_P1)
        if validateWin(picPlay,PIECE_P1):
            drawBoard(picPlay)
            print("Player 1 Wins")
            GameOver = True
        Player = 2
        turn += 1

    else:
        print("Player No: ",Player)
        actSelect = int(input("Please enter the column to drop tile:(1-7) "))
        ColSelect = actSelect-OFFSET_VAL
        playPiece(Player,PIECE_P2)
        if validateWin(picPlay,PIECE_P2):
            drawBoard(picPlay)
            print("Player 1 Wins")
            GameOver = True
        Player = 1
        turn = 0
