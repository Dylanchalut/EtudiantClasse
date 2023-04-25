from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import listview_dialogue

class Fenetrelistview(QtWidgets.QDialog, listview_dialogue.Ui_Dialog):

    def __init__(self, parent = None):
        super(Fenetrelistview, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")

    @pyqtSlot()
    def on_pushButton_Quitter_clicked(self):
        self.close()
