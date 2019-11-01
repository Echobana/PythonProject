from tor import TORA
from resf import RESF
import db_handler
import numpy as np


# one single-channel checkerboard with flat ends
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


# channel gap
class CG(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.d_in = 2 * self.set_rin()
        self.d_out = 2 * self.set_rout()

    def set_rin(self):
        return np.sqrt(self.tor.P / (self.tor.kappa * self.fuel.i_sp * self.fuel.density * self.u * np.pi))

    def set_rout(self):
        return self.d_in + self.u * self.tor.t_w

    def set_gap_width(self):
        return (self.d_out / 2 - self.d_in / 2) / self.tor.kappa

    def set_length(self):
        pass

    def set_gap_length(self):
        pass

    def set_channel_length(self):
        pass


# end
class E(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)
        self.length = self.set_length()
        self.d_out = self.set_dout()

    def set_length(self):
        return self.u * self.tor.t_w

    def set_dout(self):
        return np.sqrt((4 * self.fuel_volume) / (np.pi * self.length))


# multicheckers
class MC(RESF):
    def __init__(self, tor, fuel, n):
        super().__init__(tor, fuel)
        self.amount = n

    def set_din(self):
        pass

    def set_dout(self):
        pass

    def set_length(self):
        pass


if __name__ == "__main__":
    fd_dict = db_handler.db_creator_ground(
        r'F:\Elizabeth\FuelData\data_ground_1.xlsx')  # indata path is changed, ask RD-N1
    tor = TORA(1e6, 55, 7e6, 0, 100, 100)

    fuel = fd_dict["AGC"]
    # x = RESF(tor, x)
    x = E(tor, fuel)
    print(x.critic_area)
    print(x.critic_diameter)
    print(x.length)
