#!/usr/bin/python3
""" City Class """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits BaseModel """
    state_id = ""
    name = ""
