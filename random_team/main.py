import pandas as pd
from LoadData import BaseballDataLoader
import logging
from randomizer import Randomizer


logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
    logging.debug("I'm in main!")

    output_list = list()
    output_header = ["Inning","Player","Position"]

total = 0
while total != 36:
    total = 0
    data_loader = BaseballDataLoader()
    data_loader.load_data()
    players = data_loader.get_players()
    positions = data_loader.get_positions()
    randomize_players = Randomizer(positions=positions, players=players)

    for inning in range(1, 7):
        benched_count = 0
        for player in players:
            if player.get_position_type(inning).upper() == "BENCHED":
               benched_count+=1 
            print(f"Main Inning {inning}: Player {player.full_name} is in position {player.get_position_name(inning)}, {player.get_position_type(inning)}")
        if benched_count>1:
            logging.debug(f"We have too many benched players in inning {inning}")
        logging.debug("-----------------------------------")
       

    
    for player in players:
        total=total+player.infield_count
        print(f"Player: {player.full_name}'s infield count is {player.infield_count}")
    if total != 36: 
        logging.debug(f"Wrong number of in-field positions assigned 36 expected and {total} found.")


for inning in range(1, 7):
        benched_count = 0
        for player in players:
            if player.get_position_type(inning).upper() == "BENCHED":
               benched_count+=1 
            print(f"Main Inning {inning}: Player {player.full_name} is in position {player.get_position_name(inning)}, {player.get_position_type(inning)}")
            output_list.append([inning,player.full_name,player.get_position_name(inning)])
        if benched_count>1:
            logging.warning(f"We have too many benched players in inning {inning}")
        print("-----------------------------------")
       
for player in players:
    print(f"Player: {player.full_name}'s infield count is {player.infield_count}")
if total != 36: 
    logging.warning(f"Wrong number of in-field positions assigned 36 expected and {total} found.")

df_out = pd.DataFrame(data=output_list, columns=output_header)

df_out.to_excel("data/output.xlsx")
