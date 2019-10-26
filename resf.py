from fuel import FuelDataGround
from fuel import FuelData
from engine import TORA
from engine import TOR
import charachteristics as cta


class RESF(object):
    def __init__(self, engine, fuel):
        self.engine = engine
        self.fuel = fuel

    def set_mass_flow(self):
        if type(self.engine) == TORA:
            self.thrust = self.engine.set_thrust()
        else:
            self.thrust = self.engine.P
        if type(self.fuel) == FuelDataGround:
            return self.thrust / self.fuel.i_sp
        else:
            return self.thrust / cta.set_specific_impulse(self.engine, self.fuel)
