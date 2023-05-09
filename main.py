# Importer le fichier .ui converti en .py
from PyQt5.QtGui import QStandardItemModel

from Etudiant import *
import interface_graphique_etudiant
from boite_dialogue import *
from boite_dialogue_local import *


# Importer le module sys nécessaire à l'exécution
import sys

# Importer la librairie QtWidget de Qtdesigner
from PyQt5 import QtWidgets

from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
#list_etudiant = []

def verifier_num_etudiant(p_numero):
    for elt in list_etudiant:
        if elt.Matricule == p_numero:
            return True
    return False

def cacher_labels_erreur(objet):
    objet.label_Erreur_Nom.setVisible(False)
    objet.label_Erreur_Numero.setVisible(False)
    objet.label_Erreur_Etu_Existe.setVisible(False)
    objet.label_Erreur_DNaissance.setVisible(False)
    objet.label_Erreur_Etu_Inexistant.setVisible(False)

class demoQt(QtWidgets.QMainWindow, interface_graphique_etudiant.Ui_MainWindow):
    """
    Classe demoQt qui hérite des QtWidgets et de mon interface (interface-graphique-etudiant.py)
    """
    # Attribut de classe
    def __init__(self, parent=None):
        super(demoQt, self).__init__(parent)
        self.setupUi(self) # Préparer l'interface utilisateur
        self.setWindowTitle("Gestion de scolarité") # Titre de la page
        cacher_labels_erreur(self)
        self.comboBox_Programme.setCurrentIndex(-1)


    # Gestionnaire d'événement, Lorsqu'on clique sur le boutton
    @pyqtSlot()
    def on_Button_Valider_clicked(self):
        """
        Gestionnaire d'événement du bouton valider.
        """
        cacher_labels_erreur(self)
        self.comboBox_Programme.setCurrentIndex(-1)

        etud = Etudiant()

        etud.NomEtud = self.Edit_Nom_Etudiant.text().capitalize()
        etud.Matricule = self.Edit_Numero_Etudiant.text()
        etud.DateNaiss = self.dateEdit_DNaissance.date()
        etud.Programme = self.comboBox_Programme.currentText()

        verifier_etudiant = verifier_num_etudiant(self.Edit_Numero_Etudiant.text())

        if verifier_etudiant is True and etud.Matricule != "":
            self.Edit_Numero_Etudiant.clear()
            self.label_Erreur_Etu_Existe.setVisible(True)

        if etud.NomEtud == "":
            self.Edit_Nom_Etudiant.clear()
            self.label_Erreur_Nom.setVisible(True)

        if etud.Matricule == "":
            self.Edit_Numero_Etudiant.clear()
            self.label_Erreur_Numero.setVisible(True)

        if etud.DateNaiss == "":
            self.label_Erreur_DNaissance(True)

        if etud.NomEtud != "" and etud.Matricule != "" and etud.DateNaiss != "" and verifier_etudiant is False:
            list_etudiant.append(etud)
            self.textBrowser.append(etud.__str__())
            self.Edit_Nom_Etudiant.clear()
            self.Edit_Numero_Etudiant.clear()

    @pyqtSlot()
    def on_Button_Modifier_clicked(self):
        cacher_labels_erreur(self)

        etud = Etudiant()

        etud.NomEtud = self.Edit_Nom_Etudiant.text().capitalize()
        etud.Matricule = self.Edit_Numero_Etudiant.text()
        etud.Programme = self.comboBox_Programme.currentText()

        verifier_etudiant = verifier_num_etudiant(self.Edit_Numero_Etudiant.text())

        if verifier_etudiant is False and etud.Matricule != "":
            self.Edit_Numero_Etudiant.clear()
            self.label_Erreur_Numero.setVisible(True)

        if etud.NomEtud == "":
            self.Edit_Nom_Etudiant.clear()
            self.label_Erreur_Nom.setVisible(True)

        if etud.Matricule == "":
            self.Edit_Numero_Etudiant.clear()
            self.label_Erreur_Numero.setVisible(True)

        if etud.NomEtud != "" and etud.Matricule != "" and etud.DateNaiss != "":
            for elt in list_etudiant:
               if elt.Matricule == self.Edit_Numero_Etudiant.text():
                    # Apporter les modifications aux attributs Nom_Etud, Programme et Date_Naiss
                    elt.NomEtud= self.Edit_Nom_Etudiant.text().capitalize()
                    elt.Programme = self.comboBox_Programme.currentText()
                    elt.DateNaiss = self.dateEdit_DNaissance.date()
            # Effacer le textBowser
            self.textBrowser.clear()
            # Après modifications, réafficher tous les étudiants de la liste dans le textBrowser
            for elt in list_etudiant:
                self.textBrowser.append(elt.__str__())
            # Réinitialiser les lineEdits du numéro et du nom et le dateEdit
            self.Edit_Numero_Etudiant.clear()
            self.Edit_Nom_Etudiant.clear()
            self.dateEdit_DNaissance.setDate(QDate(2000, 1, 1))

    @pyqtSlot()
    # Bouton Supprimer
    def on_Button_Supprimer_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        etud = Etudiant()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        etud.NomEtud = self.Edit_Nom_Etudiant.text().capitalize()
        etud.Matricule = self.Edit_Numero_Etudiant.text()
        etud.DateNaiss = self.dateEdit_DNaissance.date()
        etud.Programme = self.comboBox_Programme.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_etudiant = verifier_num_etudiant(self.Edit_Numero_Etudiant.text())
        # Si le numéro d'étudiant est valide, mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_etudiant is False and etud.Matricule != "":
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.Edit_Numero_Etudiant.clear()
            self.label_erreur_Etu_Inexistant.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if etud.NomEtud == "":
            self.Edit_Nom_Etudiant.clear()
            self.label_Erreur_Nom.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if etud.Matricule == "":
            self.Edit_Numero_Etudiant.clear()
            self.label_Erreur_Numero.setVisible(True)
            # Si la date de naissance est invalide, afficher un message d'erreur
        if etud.DateNaiss == "":
            self.label_Erreur_DNaissance.setVisible(True)

        # Si le nom, le numéro et la date de naissance sont valides et l'étudiant existe dans la liste des étudiants :
        if etud.NomEtud != "" and etud.Matricule != "" and etud.DateNaiss != "" and verifier_etudiant is True:
            trouve = False
            for elt in list_etudiant:
                # # Chercher dans la liste des étudiants un étudiant ayant les informations entrées
                if elt.Matricule == self.Edit_Numero_Etudiant.text() and elt.NomEtud == self.Edit_Nom_Etudiant.text().capitalize()\
                                   and elt.Programme == self.comboBox_Programme.currentText() \
                                   and elt.DateNaiss == self.dateEdit_DNaissance.date():
                    # Supprimer l'étudiant de la liste des étudiants
                    trouve = True
                    list_etudiant.remove(elt)
                    break
            # Si l'étudiant n'existe pas dans la liste afficher un message d'erreur dans le label_erreur_Etu_Inexistant
            if not trouve:
                self.label_erreur_Etu_Inexistant.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser.clear()
                for elt in list_etudiant:
                    self.textBrowser.append(elt.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.Edit_Numero_Etudiant.clear()
                self.Edit_Nom_Etudiant.clear()
                self.dateEdit_DNaissance.setDate(QDate(2000, 1, 1))

    @pyqtSlot()
    def on_Button_ListView_clicked(self):
        dialog = Fenetrelistview()

        model = QStandardItemModel()
        dialog.listView_Etudiants.setModel(model)
        for e in list_etudiant:
            item = QStandardItem(e.Matricule + " * " + e.NomEtud + " * " + e.Programme)
            model.appendRow(item)


        dialog.setModal(True)
        dialog.show()
        dialog.exec()

    @pyqtSlot()
    def on_Button_Ajouter_Local_clicked(self):
        dialog = Fenetrelistview_local()

        cacher_labels_erreur(self)

        model = QStandardItemModel()
        #dialog.listView_Etudiants.setModel(model)
        # for e in list_etudiant:
        #     item = QStandardItem(e.Matricule + " * " + e.NomEtud + " * " + e.Programme)
        #     model.appendRow(item)


        dialog.setModal(True)
        dialog.show()
        dialog.exec()

def main():
    mon_app = QtWidgets.QApplication(sys.argv)
    mon_formulaire1 = demoQt()
    mon_formulaire1.show()
    mon_app.exec()

if __name__=="__main__":
    main()
