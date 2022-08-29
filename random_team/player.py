from abc import ABC, abstractclassmethod, abstractmethod


class Player():

    @abstractmethod
    def __init__(self, name:str) -> None:
        """Loads initial information like name, and rules for the player"""
        pass
    
    @abstractmethod
    def assign_position(self, position: str) -> bool:
        """Takes a position and assigns it to the player if they are allowed based on rules"""
        pass

    def load_rule(self,position,):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class BaseballPlayer(Player):

    def __init__(self, name:str) -> None:
        self.full_name = name.strip().title()
        self.position: str
        self.num_rounds:int

    def assign_position(self, position: str) -> bool:
        pass

    def __str__(self) -> str:
        return self.full_name
