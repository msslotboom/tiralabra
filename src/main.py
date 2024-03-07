from minimax import Minimax
from connect4 import Connect4
from gameloop import GameLoop
import argparse


def run(args):
    game = Connect4()
    gameloop = GameLoop(game, args.debug)
    gameloop.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    run(args)
