from flask import Flask, request
from chess import Board
import json
app = Flask(__name__)
from chess_ai import get_best_move
@app.route("/move", methods=['POST'])
def post_move():
    try:
        request_body = json.loads(request.data)
        fen = request_body['fen']
        board = Board(fen)
        best_move = get_best_move(board)
        response = {"move":best_move.uci()}
        return json.dumps(response)
    except KeyError:
        return 'Could not find fen value', 400
    except ValueError:
        return 'The fen value is invalid', 400
    except Exception:
        return 'Unexpected Error', 500
