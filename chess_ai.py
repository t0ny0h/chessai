import chess
import random

player = chess.WHITE
score_map = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30, 
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900,
}
MAX_DEPTH = 3
def score_board(board: chess.Board):
    piece_map = board.piece_map()
    score = 0
    for key in piece_map.keys():
        piece = piece_map[key]
        if piece.color == player:
            score+=score_map[piece.piece_type]
        else:
            score-=score_map[piece.piece_type]
    return score
def get_best_move(board: chess.Board):
    return minimax(board)

def get_best_score(board: chess.Board, depth: int):
    global MAX_DEPTH, player
    if depth == MAX_DEPTH:
        return score_board(board)
    board_copy = board.copy()
    scores = []
    for move in board_copy.pseudo_legal_moves:
        board_copy.push(move)
        score = get_best_score(board_copy, depth+1)
        board_copy.pop()
        scores.append(score)

    if board.turn == player:
        return max(scores)
    return min(scores)
def minimax(board: chess.Board):
    moves = []
    board_copy = board.copy()
    for move in board_copy.pseudo_legal_moves:
        board_copy.push(move)
        best_score_for_move = get_best_score(board_copy, 0)
        moves.append((move, best_score_for_move))
        board_copy.pop()

    max_score = - 99999 
    max_score_moves = []
    for move in moves:
        if move[1]>max_score:
            max_score = move[1]
            max_score_moves = [move[0]]
        elif move[1] == max_score:
            max_score_moves.append(move[0])
    return random.choice(max_score_moves)