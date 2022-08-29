import pandas as pd
from LoadData import BaseballDataLoader
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug("I'm in main!")
    data_loader = BaseballDataLoader()
    data_loader.load_data()
    players = data_loader.get_players()
    for player in players:
        print(player)