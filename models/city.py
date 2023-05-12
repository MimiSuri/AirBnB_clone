#!/usr/bin/python3
"""City class inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    state_id = ""  # it will be the State.id
    name = ""
