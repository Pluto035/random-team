from abc import ABC, abstractmethod
from lib2to3.pytree import Base
from typing import List
from player import BaseballPlayer
from position import Position
from LoadData import DataLoader
import pandas as pd
import logging
import random


class Randomizer():

    def __init__(self, positions: List[Position], players: List[BaseballPlayer], innings=6) -> None:
        
        self.positions=positions
        self.players = players
        self.num_innings = innings
        self.final_players: List[BaseballPlayer] = list()

        

        print("Players")
        for inning in range(1, self.num_innings+1):
            # players_inning = self.players.copy()
            # positions_inning = self.positions.copy()
            random.shuffle(self.positions)
            BaseballPlayer.benched=0
            for current_position in self.positions:
                
                logging.debug(f"The current position is: {current_position.position_name} with type {current_position.position_type}")
                for player in self.players:
                    if player.allowed_position(inning, self.num_innings, current_position):
                            logging.debug(f"The allowed player is {player.full_name} for position {current_position.position_name} for inning {inning}")
                            # TODO need to create a new object here so that I don't lose the player info outside of the scope of the loop
                            player.assign_position(inning, current_position) 
                            #print(f"Inning {inning}: Player {player.full_name} is in position {player.get_position_name(inning)}, {player.get_position_type(inning)}")
                            break
                    else:
                        logging.debug(f"Inning: {inning} Player {player.full_name} is not allowed for position {current_position.position_name} and type {current_position.position_type} and infield count is {player.infield_count}")

            for player in self.players:
                if inning not in player.player_positions:
                    BaseballPlayer.benched+=1
                    player.assign_position(inning, Position("Benched", "Benched"))
                    if BaseballPlayer.benched>1:
                        print("Multiple people are benched")
            
