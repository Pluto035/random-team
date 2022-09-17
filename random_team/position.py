from abc import ABC, abstractclassmethod, abstractmethod

class Position():

    def __init__(self, position_name:str, position_type:str) -> None:
        self.position_name:str = position_name.strip().upper()
        self.position_type:str = position_type.strip().upper()
        self.assigned: bool = False

    def __lt__(self, other):
        return self.position_type < other.position_type