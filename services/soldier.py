from pydantic import BaseModel, Field

class Soldier:
    def __init__(self, ID, first_name, last_name, phone_number, rank):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    # ID:int = Field(...)
    # first_name:str = Field(...)
    # last_name:str = Field(...)
    # phone_number:int = Field(...)
    # rank:int = Field(...)