from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Local import *
from Local_Normal import *
from Local_Technique import *
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
        self.cacher_label_technique(True)
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
        self.cacher_label_erreur(False)

        L = Local()
        N = Local_Normal()
        T = Local_Technique()

        L.Type_Local = self.comboBox_type_local.currentText()
        L.Numero_Local = self.lineEdit_num_local.text().capitalize()
        L.Lieu_Local = self.comboBox_lieu_local.currentText()
        L.Dimension_Local = self.lineEdit_dimension.text()
        L.Nbr_PLaces = self.lineEdit_nb_places.text()

        N.Nb_places_tables = self.lineEdit_nb_places_table.text()

        T.Marque_ordi = self.lineEdit_marque_ordi.text()
        T.Nb_ordi = self.lineEdit_nb_ordi.text()
        T.projecteur = self.comboBox_projecteur.currentText()

        if L.Numero_Local == "":
            self.lineEdit_num_local.clear()
            self.label_erreur_num_local.setVisible(True)

        if L.Dimension_Local == "":
            self.lineEdit_dimension.clear()
            self.label_erreur_dimension.setVisible(True)

        if L.Nbr_PLaces == "":
            self.lineEdit_nb_places.clear()
            self.label_erreur_nb_place.setVisible(True)





    @pyqtSlot()
    def on_Button_Quitter_local_clicked(self):
        self.close()

