from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import BOOLEAN
from data.session import Base
class ChemicalHazards(Base):
   __tablename__="ChemicalHazards"
   id=Column(Integer, primary_key=True, autoincrement=True)
   Chemical = Column(String)
   Corrosive= Column(String, default="FALSE")
   Flammable= Column(String, default="FALSE")
   Hazardous= Column(String, default="FALSE")
   Environment= Column(String, default="FALSE")
   Respiratory= Column(String, default="FALSE")
   Toxic= Column(String, default="FALSE")
   HHM= Column(String, default="FALSE")

   def __init__(self, Chemical, Corrosive, Flammable, Hazardous, Environment, Respiratory, Toxic, HHM):
          self.Chemical = Chemical
          self.Corrosive = Corrosive
          self.Flammable = Flammable
          self.Hazardous = Hazardous
          self.Environment = Environment
          self.Respiratory = Respiratory
          self.Toxic = Toxic
          self.HHM = HHM
class Replacements(Base):
       __tablename__="Replacements"
       id=Column(Integer, primary_key=True, autoincrement=True)
       OldName= Column( String, unique=True)
       CorrectSpelling = Column(String, unique=True)
       def __init__(self, OldName, CorrectSpelling):
              self.OldName = OldName
              self.CorrectSpelling = CorrectSpelling
   