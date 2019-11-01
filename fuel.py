from numpy import sqrt
import charachteristics as cta

R = 8.314


class FuelData(object):
    def __init__(self, T_c, u_1, nu, density, mu_cp, k):
        self.T_c = T_c
        self.u_1 = u_1
        self.nu = nu
        self.density = density
        self.mu_cp = mu_cp
        self.k = k
        self.R_c = R / mu_cp
        self.a = sqrt(self.k) * (2 / (self.k + 1)) ** ((self.k + 1) / (2 * (self.k - 1)))
        self.beta = sqrt(self.R_c * self.T_c) / self.a
        self.critic_speed = self.set_critic_sonic_speed()

    def set_critic_sonic_speed(self):
        return sqrt(2 * self.k / (self.k + 1) * self.R_c * self.T_c)


class FuelDataGround(FuelData):
    def __init__(self, T_c, u_1, nu, density, mu_cp, k, beta, i_sp):
        super().__init__(T_c, u_1, nu, density, mu_cp, k)
        self.i_sp = i_sp
        self.beta = beta


class FuelDataSol(FuelDataGround):
    def __init__(self, T_c, u_1, nu, density, mu_cp, k, beta, i_sp, z, w, v):
        super().__init__(T_c, u_1, nu, density, mu_cp, k, beta, i_sp)
        self.w = w
        self.v = v
        self.z = z


if __name__ == "__main__":
    pass
