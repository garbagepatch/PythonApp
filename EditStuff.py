from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget
from ChangeStuffDialog import Ui_HazardTable
from PySide2.QtWidgets import QDialog
from PySide2 import QtGui, QtCore
import sqlalchemy as db
from models.Hazard import ChemicalHazards
from data.session import Session

class EditStuff(QDialog, Ui_HazardTable):
    def __init__(self, parent= None):
        self.session = Session()
        self.chemicalHazards = self.session.query(ChemicalHazards).all()

        








class HazardModel(QAbstractTableModel):
    def __init__(self, parent, *args):
        results =connection.execute(db.select(['ChemicalHazards']))