from positionvalues import *

personalitydict={"standard":(position_values_standard,piece_values_standard), \
    "agressive":(position_values_agressive,piece_values_agressive)} #from positionvalues.py
"""Section 3.1: Evaluation"""
def positionEvaluation(position, piece_values, position_values):    #returns the value of the input board in term of pawn advantage for white
    other=otherEvaluation(position)
    material=materialEvaluation(position,piece_values)
    position=posEvaluation(position,position_values)
    return material+position+other
def materialEvaluation(position,piece_values):                      #returns the value of the material
    resultvalue=0
    for row in range(8):
        for col in range(8):
            piece=position[row][col]
            if piece==None:
                pass
            else:
                if piece.color=="white":
                    value=piece_values[f'{piece.ty}']
                    resultvalue+=value
                if piece.color=="black":
                    value=piece_values[f'{piece.ty}']
                    resultvalue-=value
    return resultvalue
def posEvaluation(position,position_values):                        #returns the value of the material under a given position
    whiteeval=0
    blackeval=0
    for row in range(8):
        for col in range(8):
            piece=position[row][col]
            if piece==None:
                pass
            else:
                if piece.color=="white":
                    valuetable=position_values[f'{piece.ty}']
                    whiteeval+=valuetable[row][col]
                if piece.color=="black":
                    valuetable=position_values[f'{piece.ty}']
                    blackeval+=valuetable[7-row][col]
    return whiteeval-blackeval
def otherEvaluation(position):                                      #returns the value of other factors that could effect advantage
    vmwhite=validMoves(position,"white")
    vmblack=validMoves(position,"black")
    #central pawns
    whitecentralpawns=0
    blackcentralpawns=0
    for i in range(3,5):
        for j in range(3,5):
            if board[i][j]==None:
                pass
            elif board[i][j].color=="white":
                whitecentralpawns+=1.5
            elif board[i][j].color=="black":
                blackcentralpawns+=1.5
    #connected rooks
    whiterooks=0
    blackrooks=0
    if WKR.x == WQR.x or WKR.y==WQR.y:
        whiterooks+=1
    if BKR.x == BQR.x or BKR.y==BQR.y:
        blackrooks+=1
    #development
    whitedev=0
    blackdev=0
    for piece in vmwhite:
        for move in vmwhite[piece]:
            whitedev+=.2
    for piece in vmblack:
        for move in vmblack[piece]:
            blackdev+=.2
    #doubled pawns:
    whitedubs=0
    blackdubs=0
    for i in range(8):
        for j in range(7):
            if board[i][j]==None or board[i][j+1]==None:
                continue
            if (board[i][j].ty!="Pawn") or (board[i][j+1].ty!="Pawn"):
                continue
            elif board[i][j].color=="white":
                whitedubs-=.5
            elif board[i][j].color=="black":
                blackdubs-=.5
    #vulnerable king:
    whiteking=0
    blackking=0
    if 3<WKK.x<5:
        whiteking-=1
    if WKK.y>2:
        whiteking-=3
    if 3<BKK.x<5:
        blackking-=1
    if BKK.y<6:
        blackking-=3
    #bishoppair:
    whitebishop=0
    blackbishop=0
    if WKB.alive and WQB.alive:
        whitebishop+=1.2
    if BKB.alive and BQB.alive:
        whitebishop+=1.2
    whitetotal=whitecentralpawns+whiterooks+whitedubs+whiteking+whitebishop
    blacktotal=blackcentralpawns+blackrooks+blackdubs+blackking+blackbishop
    return whitetotal-blacktotal
"""Section 3.2: Minimax"""
def getBestMoveMinimax(app, position,personality):  #loops through all possible moves in the position, and finds the best move as evaluated from minimax
    start=time.time()
    depth=2
    pival=personalitydict[personality][1]
    poval=personalitydict[personality][0]
    bestmove=0
    bestpiece=0
    bestscore=10000
    movedict=validMoves(position,"black")
    for piece in movedict:
        for moves in movedict[piece]:
            copyboard=copy.deepcopy(position)
            movePieceforEval(piece,moves,copyboard)
            score=minimax(copyboard,depth,True,pival,poval)
            if score<bestscore:
                bestscore=score
                bestmove=moves
                bestpiece=piece
    end=time.time()
    #print(f"minimax depth {depth} took {end-start}")
    return (bestpiece,bestmove)
def minimax(position, depth, maximizing, piece_values, position_values):
    if depth == 0:
        return positionEvaluation(position, piece_values, position_values)
    if maximizing:
        maxEval = -10000
        movedict=validMoves(position,"black")
        for piece in movedict:
            for moves in movedict[piece]:
                boardcopy=copy.deepcopy(position)
                movePieceforEval(piece,moves,boardcopy)
                score = minimax(boardcopy, depth-1, False,piece_values,position_values)
                bestscore = max(maxEval, score)
        return bestscore
    else:
        maxEval = 10000
        movedict=validMoves(position,"white")
        for piece in movedict:
            for moves in movedict[piece]:
                boardcopy=copy.deepcopy(position)
                movePieceforEval(piece,moves,boardcopy)
                score=minimax(boardcopy,depth-1,True,piece_values,position_values)
                bestscore= min(maxEval,score)
        return bestscore
"""Section 3.3 AB pruning"""
def getBestMoveAB(app, position,personality):       #loops through all possible moves in the position, and finds the best move as evaluated from abpruning
    start=time.time()
    depth=2
    pival=personalitydict[personality][1]
    poval=personalitydict[personality][0]
    bestmove=0
    bestpiece=0
    bestscore=10000
    movedict=validMoves(position,"black")
    for piece in movedict:
        for moves in movedict[piece]:
            copyboard=copy.deepcopy(position)
            movePieceforEval(piece,moves,copyboard)
            score=abpruning(copyboard,depth,-10000,10000,True,pival,poval)
            if score<bestscore:
                bestscore=score
                bestmove=moves
                bestpiece=piece
    end=time.time()
    #print(f"ab depth {depth} took {end-start}")
    return (bestpiece,bestmove)
def abpruning(position, depth, alpha, beta, maximizing, piece_values, position_values):
    if depth == 0:
        return positionEvaluation(position, piece_values, position_values)
    if maximizing:
        maxEval = -10000
        movedict=validMoves(position,"black")
        for piece in movedict:
            for moves in movedict[piece]:
                boardcopy=copy.deepcopy(position)
                movePieceforEval(piece,moves,boardcopy)
                bestscore = max(maxEval, abpruning(boardcopy, depth-1,alpha,beta,False,piece_values,position_values))
                alpha = max(alpha, bestscore)
                if beta<=alpha:
                    break
        return bestscore
    else:
        maxEval = 10000
        movedict=validMoves(position,"white")
        for piece in movedict:
            for moves in movedict[piece]:
                boardcopy=copy.deepcopy(position)
                movePieceforEval(piece,moves,boardcopy)
                bestscore=min(maxEval, abpruning(boardcopy, depth-1,alpha,beta,True,piece_values,position_values))
                bestscore= min(beta,bestscore)
                if beta<=alpha:
                    break
        return bestscore
"""Section 3.4 Eval Helpers"""
def validMoves(position,color):     #returns a dictionary with keys as pieces and valid moves and takes as values
    start=time.time()
    resultdict=dict()
    for row in range(8):
        for col in range(8):
            piece=position[row][col]
            if piece!=None and piece.color==color:
                moves=validMoveList(piece)
                takes=validTakesList(piece)
                if moves!=[] or takes!=[]:
                    resultdict[piece]=moves+takes
    end=time.time()
    #print{f"validmoves1time={end-start}"}
    return resultdict
"""Section 3.5 AI helpers"""
def movePieceforEval(piece,dest,position): #given a piece and move, along with a position, returns the position with the piece moved
    if piece.coords==None:
        return
    return replaceforEval(piece,dest,replaceforEval(None,piece.coords,position))
def replaceforEval(piece,square,position):  #helps movePiece, deals with the board 2d list, similar to normal replace
    if square==None:
        return position
    row=square[0]
    col=square[1]
    position[row].pop(col)
    position[row].insert(col,piece)
    return position
