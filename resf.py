from fuel import FuelDataGround
import charachteristics as cta
import gdf_definitions as fdf


class RESF(object):
    def __init__(self, tor, fuel):
        self.tor = tor
        self.fuel = fuel
        self.mass_flow = self.set_mass_flow()
        self.u = self.combustion_speed()
        self.rho_c = self.set_chamber_density()
        self.a_cr = self.set_critic_area()

    def set_mass_flow(self):
        if type(self.fuel) == FuelDataGround:
            return self.tor.P / self.fuel.i_sp
        else:
            return self.tor.P / cta.set_specific_impulse(self.tor, self.fuel)

    def combustion_speed(self):
        return self.fuel.u_1 * (self.tor.p_c / 98066.5) ** self.fuel.nu

    def set_chamber_density(self):
        return self.tor.p_c / (self.fuel.R_c * self.fuel.T_c)

    def set_critic_area(self):
        return self.mass_flow / (self.rho_c * fdf.density(1, self.fuel.k) * self.fuel.a_cr)


if __name__ == "__main__":
    pass
