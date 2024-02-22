from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/move/<fen>")
def get_move(fen):
    response = {"fen":fen}
    return json.dumps(response)
@app.route("/move", methods=['POST'])
def post_move():
    request_body = json.loads(request.data)
    fen = request_body.get('fen')
    return json.dumps({'moves': fen})