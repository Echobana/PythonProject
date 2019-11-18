from fuel import FuelDataGround
from fuel import FuelDataSol
import charachteristics as cta
import gdf_definitions as fdf
import numpy as np


class RESF(object):
    def __init__(self, tor, fuel):
        self.tor = tor
        self.fuel = fuel
        self.mass_flow = self.set_mass_flow()
        self.u = self.combustion_speed()
        if type(fuel) == FuelDataSol:
            self.rho_c = self.fuel.v
        else:
            self.rho_c = self.set_chamber_density()
        self.critic_area = self.set_critic_area()
        self.critic_diameter = self.set_critic_diameter()
        self.fuel_mass = self.set_fuel_mass()
        self.fuel_volume = self.set_fuel_volume()

    def set_mass_flow(self):
        if type(self.fuel) == FuelDataGround:
            return self.tor.P / self.fuel.i_sp
        elif type(self.fuel) == FuelDataSol:
            return self.tor.P / self.fuel.i_sp
        else:
            return self.tor.P / cta.set_specific_impulse(self.tor, self.fuel)

    def combustion_speed(self):
        return self.fuel.u_1 * (self.tor.p_c / 98066.5) ** self.fuel.nu

    def set_chamber_density(self):
        if type(self.fuel) == FuelDataSol:
            return 1 / self.fuel.v
        else:
            return self.tor.p_c / (self.fuel.R_c * self.fuel.T_c)

    def set_critic_area(self):
        return self.mass_flow / (self.rho_c * fdf.density(1, self.fuel.k) * self.fuel.critic_speed)

    def set_critic_diameter(self):
        return np.sqrt(4 * self.critic_area / np.pi)

    def set_fuel_mass(self):
        return self.mass_flow * self.tor.t_w

    def set_fuel_volume(self):
        return self.fuel_mass / self.fuel.density

    def set_combustion_area(self):
        return ((self.tor.p_c ** (1 - self.fuel.nu)) * self.critic_area) / (
                self.fuel.density * self.fuel.u_1 * self.fuel.beta / (98066.5 ** self.fuel.nu))


if __name__ == "__main__":
    pass
