import requests
from chess import Board
import urllib.parse
board = Board()
fen = board.fen()
myobj = {'fen': fen}
r=requests.post('http://127.0.0.1:5000/move', json = myobj)
print(r)
print(r.text)

