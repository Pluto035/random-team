from abc import ABC, abstractclassmethod, abstractmethod
from typing import Dict
from position import Position
import logging

logging.basicConfig(level=logging.WARNING)

class Player():

    @abstractmethod
    def __init__(self, name:str) -> None:
        """Loads initial information like name, and rules for the player"""
        pass
    
    @abstractmethod
    def assign_position(self, position: Position) -> bool:
        """Takes a position and assigns it to the player if they are allowed based on rules"""
        pass

    def load_rule(self,position):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class BaseballPlayer(Player):

    benched:int = 0
    max_infield: int = 0
    team_infield_count: Dict[str, int] = dict()

    def __init__(self, name:str) -> None:
        self.full_name = name.strip().title()
        self.player_positions: Dict[int, Position] = dict()
        self.infield_count:int = 0
        BaseballPlayer.team_infield_count[self.full_name]=0

    def assign_position(self,inning:int, position: Position) -> None:
        self.player_positions[inning]=Position(position.position_name, position.position_type)
        if self.player_positions[inning].position_type == "INFIELD":
            self.infield_count+=1
            BaseballPlayer.team_infield_count[self.full_name]=self.infield_count
            if self.infield_count > self.max_infield:
                BaseballPlayer.max_infield= self.infield_count
        logging.debug(f"The assigned position in assign_position: {self.player_positions[inning].position_name}")

    def get_position_name(self,inning:int) -> str:
            return self.player_positions[inning].position_name

    
    def get_position_type(self,inning:int) -> str:
            return self.player_positions[inning].position_type
      
    def allowed_position(self,inning:int, max_inning:int, position:Position) -> bool:
        logging.debug(f"The passed parameters are {inning}, {max_inning}, and Position {position.position_name}, {position.position_type}")
        if inning not in self.player_positions:
            if position.position_type == "INFIELD" and self.infield_count<3:
                logging.debug("In Infield if statement")
                return True
            elif position.position_type == "OUTFIELD" and self.infield_count == 3:
                logging.debug("In outfield if statement equal to 3")
                return True
            elif position.position_type == "OUTFIELD" and self.infield_count < 3 and  3-self.infield_count <= (max_inning-inning):
                logging.debug("In outfield statement complex")
                return True
            elif min(self.team_infield_count.values())>=3:
                logging.debug(f"Player {self.full_name} has an infield count of {self.infield_count} and min across players is {min(self.team_infield_count.values())}")
                return True
            else:
                logging.debug(f"Player {self.full_name} is not eligable for position Position {position.position_name}, {position.position_type} and has an infield count of {self.infield_count} and min across players is {min(self.team_infield_count.values())}")
                return False

        else:
            return False

    def __str__(self) -> str:
        return self.full_name

    def __lt__(self, other):
         return self.infield_count < other.infield_count
