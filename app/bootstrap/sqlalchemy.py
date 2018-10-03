from sqlalchemy.orm import clear_mappers
from sqlalchemy import MetaData
from src.pp.infrastructure.repository.sqlalchemy.mapping import load_mapper_pp
from src.coins.infrastructure.repository.sqlalchemy.mapping import load_mapper_coin


metadata_app = MetaData()
clear_mappers()
load_mapper_coin(metadata_app)
load_mapper_pp(metadata_app)


def load_mapper_app():
    print("inicio el mapper!!!!!!!!!!!!")
