from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Local import *
from Local_Normal import *
from Local_Technique import *
import ajouter_local

list_local = []

def verifier_num_etudiant_local(p_num):
    for elt in list_local:
        if elt.Numero_Local == p_num:
            return True
    return False


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

    def GestionnerErreurLocal(self,p_type_l):

        if p_type_l == "Technique":
            L = Local_Technique()
        else :
            L = Local_Normal()

        L.Type_Local = self.comboBox_type_local.currentText()
        L.Numero_Local = self.lineEdit_num_local.text().capitalize()
        L.Lieu_Local = self.comboBox_lieu_local.currentText()
        try:
            L.Dimension_Local = int(self.lineEdit_dimension.text())
        except:
            self.label_erreur_dimension.setVisible(True)

        try:
            L.Nbr_PLaces = int(self.lineEdit_nb_places.text())
        except:
            self.label_erreur_nb_place.setVisible(True)


        verifier_num_local = verifier_num_etudiant_local(self.lineEdit_num_local.text().capitalize())

        if L.Numero_Local == "" and verifier_num_local is True:
            self.lineEdit_num_local.clear()
            self.label_erreur_num_local.setVisible(True)

        if L.Dimension_Local == 0.0:
            self.lineEdit_dimension.clear()
            self.label_erreur_dimension.setVisible(True)

        if L.Nbr_PLaces == 0:
            self.lineEdit_nb_places.clear()
            self.label_erreur_nb_place.setVisible(True)

        if L.Numero_Local != "" and L.Dimension_Local != 0.0 and L.Nbr_PLaces != 0 and verifier_num_local is False:
            list_local.append(L)
            self.lineEdit_num_local.clear()
            self.lineEdit_dimension.clear()
            self.lineEdit_nb_places.clear()


    @pyqtSlot()
    def on_Button_Ajouter_clicked(self):
        self.cacher_label_erreur(False)

        if self.comboBox_type_local.currentText() == "Technique":
            L = Local_Technique()

            L.type_local = self.GestionnerErreurLocal(self.comboBox_type_local.currentText())

            L.Marque_ordi = self.lineEdit_marque_ordi.text()
            try:
                L.Nb_ordi = int(self.lineEdit_nb_ordi.text())
            except:
                self.label_erreur_nb_ordi_2.setVisible(True)


            L.projecteur = self.comboBox_projecteur.currentText()


            if L.Marque_ordi == "":
                self.lineEdit_marque_ordi.clear()
                self.label_erreur_marque_ordi.setVisible(True)

            if L.Nb_ordi == 0:
                self.lineEdit_nb_ordi.clear()
                self.label_erreur_nb_ordi_2.setVisible(True)

            if L.Marque_ordi != "" and L.Nb_ordi != 0 and self.GestionnerErreurLocal(self.comboBox_type_local.currentText()):
                list_local.append(L)
                self.lineEdit_marque_ordi.clear()
                self.lineEdit_nb_ordi.clear()

        else:
            L = Local_Normal()
            try:
                L.Nb_places_tables = int(self.lineEdit_nb_places_table.text())
            except:
                self.label_erreur_nb_places_table.setVisible(True)


            if L.Nb_places_tables == 0:
                self.lineEdit_nb_places_table.clear()
                self.label_erreur_nb_places_table.setVisible(True)

            if L.Nb_places_tables != 0 and self.GestionnerErreurLocal():
                list_local.append(L)
                self.lineEdit_nb_places_table.clear()






    @pyqtSlot()
    def on_Button_Quitter_local_clicked(self):
        self.close()

