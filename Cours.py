from Etudiant import *

class Cours:
    """
    Classe Cours
    """
    def __init__(self, p_sigle_cours: str ="", p_titre_cours: str ="", p_nombres_heures_cours: int =0, p_etudiant: Etudiant = Etudiant()):
        self._sigle_cours = p_sigle_cours
        self._titre_cours = p_titre_cours
        self._nombre_heures_cours = p_nombres_heures_cours
        self.Etudiant = p_etudiant

    def _get_sigle_cours(self):
        return self._sigle_cours
    def _set_sigle_cours(self, v_sigle):
        if v_sigle[0].isalpha() and v_sigle[1:5].isnumeric() and len(v_sigle) == 5:
            self._sigle_cours = v_sigle
    Sigle = property(_get_sigle_cours, _set_sigle_cours)

    def _get_titre_cours(self):
        return self._titre_cours
    def _set_titre_cours(self, v_titre):
        if v_titre.isalpha() and len(v_titre) < 60:
            self._titre_cours = v_titre
    Titre = property(_get_titre_cours, _set_titre_cours)

    def _get_nombre_heures_cours(self):
        return self._nombre_heures_cours
    def _set_nombre_heures_cours(self, v_nb_heures):
        if v_nb_heures > 0:
            self._nombre_heures_cours = v_nb_heures
    Nb_heures = property(_get_nombre_heures_cours, _set_nombre_heures_cours)

