import json


class Etudiant:
    """
    Classe Etudiant
    """

    def __init__(self, p_numero : str = "", p_nom : str = "", p_programme : str = "", p_date_naiss = ""):
        """
        Constructeur de la classe Etuditant
        :param p_Numero: Le numéro de l'étudiant
        :param p_Nom: Le nom de l'étudiant
        :param p_Programme: Le programme de l'étudiant
        """
        self._numero = p_numero
        self._nom = p_nom
        self.Programme = p_programme
        self._date_naiss = p_date_naiss


    def _get_numero(self):
        return self._numero
    def _set_numero(self, v_numero):
        if len(v_numero) == 7 and v_numero.isnumeric():
            self._numero = v_numero
    Matricule = property(_get_numero, _set_numero)

    def _get_nom(self):
        return self._nom
    def _set_nom(self, v_nom):
        if len(v_nom) <= 25 and v_nom.isalpha():
            self._nom = v_nom
    NomEtud = property(_get_nom, _set_nom)

    def _get_date_naiss(self):
        """
        Accesseur de l'attribut privé _date_naiss
        :return: attitude _date_naiss
        """
        return self._date_naiss
    def _set_date_naiss(self, p_date_naiss):
        """
        Mutateur de l'attribut privé _date_naiss
        :param v_date_naiss:
        :return:
        """
        if self.age(p_date_naiss) >= 18:
            self._date_naiss = p_date_naiss

    DateNaiss = property(_get_date_naiss, _set_date_naiss)

    def age(self, p_date_naiss):
        import datetime
        today = datetime.date.today()
        return today.year - p_date_naiss.year() - ((today.month, today.day) < (p_date_naiss.month(), p_date_naiss.day()))





    def serialiser_etudiant(self, p_fichier):
        """
        Métode de serialiser un objet de la classe Etudiant
        :param p_fichier: Le nom du fichier qui contiendra l'objet serialsier
        :return: retourne 0 si le fichier est ouvert et les informations y sont écrites,
        1 s'il y a erreur d'écriture et 2 s'il y a erreur ouverture
        """
        self.__dict__["_Etudiant__date_naiss"] = str(self.DateNaiss.year()) + "-" + \
              str(self.DateNaiss.month()) + "-" + str(self.DateNaiss.day())
        try:
            with open(p_fichier, "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2










    def __str__(self):
     chaine = "Numero d'étudiant : " + self._numero + "\n" +\
              "Nom de l'étudiant : " + self._nom + "\n" +\
              "Programme de l'étudiant : " + self.Programme + "\n" +\
              "Date de naissance : " +str(self.DateNaiss.day()) + "-" + \
              str(self.DateNaiss.month()) + "-" + str(self.DateNaiss.year()) +\
              "\n" +\
              "************************************" + "\n"
     return chaine



