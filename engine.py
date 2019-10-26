import gdf_definitions as fdf
from fuel import FuelData
from fuel import FuelDataGround
import charachteristics as cta


class TOR(object):
    def __init__(self, P, t_w, p_c, p_h, p_a, kappa):
        self.p_c = p_c
        self.P = P
        self.t_w = t_w
        self.p_h = p_h
        self.p_a = p_a
        self.kappa = kappa

    def set_la(self, fuel):
        return fdf.find_la_p(fuel.k, self.p_a, self.p_c)


class TORA(object):
    def __init__(self, I_t, t_w, p_c, p_h, f_a):
        self.I_t = I_t
        self.t_w = t_w
        self.p_c = p_c
        self.p_h = p_h
        self.f_a = f_a

    def set_thrust(self):
        return self.I_t / self.t_w

    def set_la(self, fuel):
        return fdf.find_la_q(fuel.k, 1, self.f_a)


if __name__ == "__main__":
    pass
