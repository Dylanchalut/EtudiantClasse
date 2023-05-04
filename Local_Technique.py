import Local as M
from Local import *

class Local_Technique(M.Local):
    """

    """
    def __init__(self, p_type_local : str = "", p_num_local : str = "", p_lieu_local : str = "",
                 p_dimension_local: float = 0.0, p_nbr_places: int = 0, p_marque_ordi : str = "",
                 p_nb_ordi : int = 0, p_projecteur = None):
        """
        :param p_type_local:
        :param p_num_local:
        :param p_lieu_local:
        :param p_dimension_local:
        :param p_nbr_places:
        :param p_marque_ordi:
        :param p_nb_ordi:
        :param p_projecteur:
        """
        M.Local.__init__(self, p_type_local, p_num_local, p_lieu_local, p_dimension_local, p_nbr_places)
        self._marque_ordi = p_marque_ordi
        self._nb_ordi = p_nb_ordi
        self.projecteur = p_projecteur

    def get_marque_ordi(self):
        return self._marque_ordi
    def set_marque_ordi(self, v_marque):
        if len(v_marque) < 100:
            self._marque_ordi = v_marque
    Marque_ordi = property(get_marque_ordi, set_marque_ordi)

    def get_nb_ordinateur(self):
        return self._nb_ordi
    def set_nb_ordinateur(self, v_nb_ordi):
        if v_nb_ordi > 0 and v_nb_ordi < 25:
            self._nb_ordi = v_nb_ordi
    Nb_ordi = property(get_nb_ordinateur, set_nb_ordinateur)
