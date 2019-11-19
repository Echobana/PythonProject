from tor import TORA
from resf import RESF
import db_handler
import numpy as np


# one single-channel checkerboard with flat ends, armored ends
class OSCCWFE(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.d_in = self.set_din()
        self.d_out = self.set_dout()
        self.length = self.set_length()

    def set_din(self):
        return -self.u * self.tor.t_w + np.sqrt(
            (self.u * self.tor.t_w) * (self.u * self.tor.t_w) + 2 * self.mass_flow / (
                    np.pi * self.fuel.density * self.tor.kappa * self.u))

    def set_dout(self):
        return self.d_in + 4 * self.u * self.tor.t_w

    def set_length(self):
        return 0.25 * self.tor.kappa * self.d_in


# channel gap, armored end, armored outer surface
class CGFE(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.d_in = 2 * self.set_rin()
        self.d_out = 2 * self.set_rout()
        self.b = self.set_gap_width()
        self.length = self.set_length()
        self.gap_length = self.set_gap_length()

    def set_rin(self):
        return np.sqrt(self.tor.P / (self.tor.kappa * self.fuel.i_sp * self.fuel.density * self.u * np.pi))

    def set_rout(self):
        return self.d_in / 2 + self.u * self.tor.t_w

    def set_gap_width(self):
        return (self.d_out / 2 - self.d_in / 2) / self.tor.kappa

    def set_length(self):
        return self.mass_flow * self.tor.t_w / (
                np.pi * self.fuel.density * 0.25 * (self.d_out * self.d_out - self.d_in * self.d_in))

    def set_gap_length(self):
        return self.length - self.mass_flow / (self.fuel.density * self.u * 2 * np.pi * self.d_in / 2)


# end, armored outer surface
class E(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.length = self.set_length()
        self.d_out = self.set_dout()

    def set_length(self):
        return self.u * self.tor.t_w

    def set_dout(self):
        return np.sqrt((4 * self.fuel_volume) / (np.pi * self.length))


# multicheckers, armored ends
class MC(RESF):
    def __init__(self, tor, fuel, n):
        super().__init__(tor, fuel)
        self.amount = n
        self.d_in = self.set_din()
        self.d_out = self.set_dout()
        self.length = self.set_length()

    def set_din(self):
        return -self.u * self.tor.t_w + np.sqrt(
            (self.u * self.tor.t_w) * (self.u * self.tor.t_w) + 2 * self.mass_flow / (
                    self.amount * np.pi * self.fuel.density * self.tor.kappa * self.u))

    def set_dout(self):
        return 3 * self.u * self.tor.t_w + np.sqrt(
            (self.u * self.tor.t_w) * (self.u * self.tor.t_w) + 2 * self.mass_flow / (
                    self.amount * np.pi * self.fuel.density * self.tor.kappa * self.u))

    def set_length(self):
        return 0.25 * self.tor.kappa * self.d_in


class TFE(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.d_checker = self.set_d_checker()
        self.d_in = self.set_din()
        self.d_out = self.set_dout()
        self.length = self.set_length()

    def set_d_checker(self):
        return 2 * self.u * self.tor.t_w

    def set_din(self):
        return np.sqrt((2 * self.u * self.tor.t_w) * (2 * self.u * self.tor.t_w) + 4 * self.mass_flow / (
                self.u * self.fuel.density * self.tor.kappa * np.pi))

    def set_dout(self):
        return 2 * self.u * self.tor.t_w + self.d_in

    def set_length(self):
        return self.mass_flow / (self.fuel.density * np.pi * self.u * self.d_out)


if __name__ == "__main__":
    fd_dict = db_handler.db_creator_ground_m(
        r'F:\Elizabeth\FuelData\data_ground_2.xlsx')  # indata path is changed, ask RD-N1
    tor = TORA(1e6, 55, 7e6, 0, 100, 100)
    fuel = fd_dict['AGC']

    rocket = OSCCWFE(tor, fuel)
    # print(rocket.fuel.u_1 * ((rocket.tor.p_c / 98066.5) ** rocket.fuel.nu))
    print(rocket.combustion_area)
    print(rocket.d_in*1e3)
