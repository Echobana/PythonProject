import gdf_definitions as fdf
from fuel import FuelData


class A_EngineData(object):
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
    my_engine = A_EngineData(1000, 55, 7, 0, 100)
    my_fuel = FuelData(2327, 0.7e-3, 0.7, 1800, 1000, 1.19)
    x = my_engine.set_la(my_fuel)
    print(x)
