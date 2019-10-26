from numpy import sqrt

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


class FuelDataGround(FuelData):
    def __init__(self, T_c, u_1, nu, density, mu_cp, k, beta, i_sp):
        super().__init__(T_c, u_1, nu, density, mu_cp, k)
        self.i_sp = i_sp
        self.beta = beta


if __name__ == "__main__":
    pass
