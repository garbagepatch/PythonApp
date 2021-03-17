from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget
from ChangeStuffDialog import Ui_HazardTable
from PySide2.QtWidgets import QDialog
from PySide2 import QtGui, QtCore
import sqlalchemy as db
from models.Hazard import ChemicalHazards, Replacements
from data.session import Session
from models.alchemical_model import AlchemicalTableModel
class EditStuff(QDialog, Ui_HazardTable):
    def __init__(self, parent= None):
        self.session = Session()
        self.chemicalHazards = self.session.query(ChemicalHazards).all()
        self.replacements = self.session.query(Replacements).all()
        self.model = AlchemicalTableModel(
            self.session,
            ChemicalHazards,
            [
            ('Chemical Name', ChemicalHazards.Chemical, 'Chemical',{}),
            ('Corrosive', ChemicalHazards.Corrosive, 'Corrosive',{})

            ])
        table = QTableView(parent)
        table.setModel(self.model)

        








