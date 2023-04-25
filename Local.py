class Local:
    """
    Classe Local
    """
    def __init__(self, p_type_local : str = "", p_num_local : str = "", p_lieu_local : str = "",
                 p_dimension_local: float = 0.0, p_nbr_places: int = 0):
        """
        :param p_type_local:
        :param p_num_local:
        :param p_lieu_local:
        :param p_dimension_local:
        :param p_nbr_places:
        """
        self.Type_Local = p_type_local
        self._num_local = p_num_local
        self.Lieu_Local = p_lieu_local
        self._dimension_local = p_dimension_local
        self._nbr_places = p_nbr_places

    def get_num_local(self):
        return self._num_local
    def set_num_local(self, v_numero):
        if v_numero[0].isalpha() and v_numero[1] == "-" and v_numero[2:3:4].isnumeric and len(v_numero) == 5:
            self._num_local = v_numero
    Numero_Local = property(get_num_local, set_num_local)

    def get_dimension_local(self):
        return self._dimension_local
    def set_dimension_local(self, v_dimension):
        if v_dimension > 0 and v_dimension.isnumeric:
            self._dimension_local = v_dimension
    Dimension_Local = property(get_dimension_local, set_dimension_local)

    def get_nbr_places(self):
        return self._dimension_local
    def set_nbr_places(self, v_places):
        if v_places > 0 and v_places < 25  and v_places.isnumeric:
            self._dimension_local = v_places
    Nbr_PLaces = property(get_nbr_places, set_nbr_places)
