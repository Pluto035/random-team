from abc import ABC, abstractmethod
from typing import List
from player import Player, BaseballPlayer
import pandas as pd
import logging


class DataLoader(ABC):
    
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def get_players(self) -> List[Player]:
        pass

    @abstractmethod
    def get_positions(self) -> List[str]:
        pass


class BaseballDataLoader(DataLoader):

    def __init__(self) -> None:
        self.player_data: pd.DataFrame
        self.player_data_row: list
        self.players: list = list()

        self.position_data: pd.DataFrame
        self.position_data_row: list
        self.positions: list = list()


    def load_data(self):
        logging.debug("I am in load_data")
        file = pd.read_excel(io = "data\Baseball_Roster.xlsx", sheet_name=None)
        
        self.player_data = file["Players"]
        logging.debug(f"The data in self.player_data is: {self.player_data}.")

        self.position_data =  file["Positions"]
        logging.debug(f"The data in self.position_data is: {self.position_data}.")

    def get_players(self) -> List[BaseballPlayer]:
        self.player_data_row = self.player_data.values.tolist()
        logging.debug(f"The value of self.name_list is: {self.player_data_row}")
        for row in self.player_data_row:
            logging.debug(f"The value of row is: {row}")
            name = row[0]
            logging.debug(f"The value of name is: {name}")
            self.players.append(BaseballPlayer(name))
        return self.players

    def get_positions(self) -> List[str]:
        self.player_data_row = self.player_data.values.tolist()
        logging.debug(f"The value of self.name_list is: {self.player_data_row}")