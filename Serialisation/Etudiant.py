import json

class Etudiant:
    """
    Classe Etudiant
    """

    def __init__(self, p_numero : str = "", p_nom : str = "", p_programme : str = ""):                     #p_date_naiss = ""
        """
        Constructeur de la classe Etuditant
        :param p_Numero: Le numéro de l'étudiant
        :param p_Nom: Le nom de l'étudiant
        :param p_Programme: Le programme de l'étudiant
        """
        self._numero = p_numero
        self._nom = p_nom
        self.Programme = p_programme
        #self._date_naiss = p_date_naiss


    def get_numero(self):
        return self._numero
    def set_numero(self, v_numero):
        if len(v_numero) == 7 and v_numero.isnumeric:
            self._numero = v_numero
    Matricule = property(get_numero, set_numero)

    def get_nom(self):
        return self._nom
    def set_nom(self, v_nom):
        if len(v_nom) <= 25 and v_nom.isalpha():
            self._nom = v_nom
    NomEtud = property(get_nom, set_nom)

    def serialiser(self, p_fichier):
        with open(p_fichier, "w") as fichier :
            json.dump(self.__dict__, fichier)

    def deserialiser(self, p_fichier):
        with open(p_fichier, "r") as fichier :
            self.__dict__ = json.load(fichier)







#    def get_date_naiss(self):
 #       """
  #      Accesseur de l'attribut privé _date_naiss
   #     :return: attitude _date_naiss
    #    """
     #   return self._date_naiss
    #def set_date_naiss(self, p_date_naiss):
     #   """
      #  Mutateur de l'attribut privé _date_naiss
       # :param v_date_naiss:
       # :return:
        #"""
        #if self.age(p_date_naiss) >= 18:
         #   self._date_naiss = p_date_naiss

  #  DateNaiss = property(get_date_naiss, set_date_naiss)

   # def age(self, p_date_naiss):
    #    import datetime
     #   today = datetime.date.today()
      #  return today.year - p_date_naiss.year() - ((today.month, today.day) < (p_date_naiss.month(), p_date_naiss.day()))

    def __str__(self):
     chaine = "Numero d'étudiant : " + self._numero + "\n" +\
              "Nom de l'étudiant : " + self._nom + "\n" +\
              "Programme de l'étudiant : " + self.Programme + "\n" +\
              "************************************" + "\n"
     return chaine

#"Date de naissance : " +str(self.DateNaiss.day()) + "-" + \
 #             str(self.DateNaiss.month()) + "-" + str(self.DateNaiss.year()) +\
  #            "\n" +\

