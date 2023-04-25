import Local as M
from Local import *

class Local_Normal(M.Local):
    """

    """
    def __init__(self, p_type_local : str = "", p_num_local : str = "", p_lieu_local : str = "",
                 p_dimension_local: float = 0.0, p_nbr_places: int = 0, p_nb_tables : int = 0):
        """
        :param p_type_local:
        :param p_num_local:
        :param p_lieu_local:
        :param p_dimension_local:
        :param p_nbr_places:
        :param p_nb_tables:
        """
        M.Local.__init__(self, p_type_local, p_num_local, p_lieu_local, p_dimension_local, p_nbr_places)
        self._nb_places_tables = p_nb_tables

    def get_nb_places_tables(self):
        return self._nb_places_tables
    def set_nb_places_tables(self, v_places_tables):
        if v_places_tables.isnumeric and v_places_tables == 1 or v_places_tables == 2:
            self._nb_places_tables = v_places_tables
    Nb_places_tables = property(get_nb_places_tables, set_nb_places_tables)
