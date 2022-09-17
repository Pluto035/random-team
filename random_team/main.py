import pandas as pd
from LoadData import BaseballDataLoader
import logging
from randomizer import Randomizer


logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
    logging.debug("I'm in main!")
    data_loader = BaseballDataLoader()
    data_loader.load_data()
    players = data_loader.get_players()
    positions = data_loader.get_positions()

    randomize_players = Randomizer(positions=positions, players=players)

    for inning in range(1, 7):
        for player in players:
            print(f"Main Inning {inning}: Player {player.full_name} is in position {player.get_position_name(inning)}, {player.get_position_type(inning)}")
        print("-----------------------------------")

    for player in players:
        print(f"Player: {player.full_name}'s infield count is {player.infield_count}")
