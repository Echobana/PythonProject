import gdf_definitions as fdf


class typeTOR(object):
    def __init__(self, t_w, p_c, p_h, kappa):
        self.p_c = p_c
        self.t_w = t_w
        self.p_h = p_h
        self.kappa = kappa


class TOR(typeTOR):
    def __init__(self, P, t_w, p_c, p_h, p_a, kappa):
        super().__init__(t_w, p_c, p_h, kappa)
        self.P = P
        self.p_a = p_a

    def set_la(self, fuel):
        return fdf.find_la_p(fuel.k, self.p_a, self.p_c)


class TORA(typeTOR):
    def __init__(self, I_t, t_w, p_c, p_h, f_a, kappa):
        super().__init__(t_w, p_c, p_h, kappa)
        self.I_t = I_t
        self.f_a = f_a
        self.P = self.I_t / self.t_w

    def set_la(self, fuel):
        return fdf.find_la_q(fuel.k, 1, self.f_a)


if __name__ == "__main__":
    pass
