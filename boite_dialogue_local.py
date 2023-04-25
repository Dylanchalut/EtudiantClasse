from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import ajouter_local

list_local = []



class Fenetrelistview_local(QtWidgets.QDialog, ajouter_local.Ui_Dialog):

    def cacher_label_erreur(self, B):
        self.label_erreur_num_local.setVisible(B)
        self.label_erreur_dimension.setVisible(B)
        self.label_erreur_nb_place.setVisible(B)
        self.label_erreur_marque_ordi.setVisible(B)
        self.label_erreur_nb_ordi_2.setVisible(B)
        self.label_erreur_nb_places_table.setVisible(B)

    def cacher_label_normal(self, B):
        self.label_nb_places_table.setVisible(B)
        self.lineEdit_nb_places_table.setVisible(B)

    def cacher_label_technique(self, B):
        self.comboBox_projecteur.setVisible(B)
        self.label_projecteur.setVisible(B)
        self.lineEdit_nb_ordi.setVisible(B)
        self.label_nb_ordi.setVisible(B)
        self.lineEdit_marque_ordi.setVisible(B)
        self.label_marque_ordi.setVisible(B)


    def __init__(self, parent=None):
        super(Fenetrelistview_local, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un local")
        self.cacher_label_erreur(False)
        self.cacher_label_technique(False)
        self.cacher_label_normal(False)
        self.comboBox_type_local.currentIndexChanged.connect(self.affiche_widget)

    def affiche_widget(self):
        if self.comboBox_type_local.currentText() == "Technique":
            self.cacher_label_technique(True)
            self.cacher_label_normal(False)
        else:
            self.cacher_label_technique(False)
            self.cacher_label_normal(True)

    @pyqtSlot()
    def on_Button_Ajouter_clicked(self):
        pass


    @pyqtSlot()
    def on_Button_Quitter_local_clicked(self):
        self.close()

