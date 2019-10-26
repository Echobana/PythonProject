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

    def set_beta(self):
        return sqrt(self.R_c * self.T_c) / self.set_a()

    def set_a(self):
        return sqrt(self.k) * (2 / (self.k + 1)) ** ((self.k + 1) / (2 * (self.k - 1)))

    def u_combustion(self, p):
        return self.u_1 * (p / 98066.5) ** self.nu


class FuelDataGround(object):
    def __init__(self, T_c, u_1, nu, density, mu_cp, beta, k, i_sp):
        self.T_c = T_c
        self.u_1 = u_1
        self.nu = nu
        self.density = density
        self.beta = beta
        self.k = k
        self.i_sp = i_sp
        self.mu_cp = mu_cp


if __name__ == "__main__":
    pass
