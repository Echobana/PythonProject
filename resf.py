from fuel import FuelDataGround
from fuel import FuelData
from tor import TORA
from tor import TOR
import charachteristics as cta


class RESF(object):
    def __init__(self, tor, fuel):
        self.tor = tor
        self.fuel = fuel
        self.mass_flow = self.set_mass_flow()
        self.u = self.combustion_speed()

    def set_mass_flow(self):
        if type(self.tor) == TORA:
            self.thrust = self.tor.set_thrust()
        else:
            self.thrust = self.tor.P
        if type(self.fuel) == FuelDataGround:
            return self.thrust / self.fuel.i_sp
        else:
            return self.thrust / cta.set_specific_impulse(self.tor, self.fuel)

    def combustion_speed(self):
        return self.fuel.u_1 * (self.tor.p_c / 98066.5) ** self.fuel.nu


if __name__ == "__main__":
    pass
