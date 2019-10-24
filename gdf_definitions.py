from numpy import sqrt
from scipy.optimize import fsolve


def a_gdf(k):
    return sqrt(k) * (2 / (k + 1)) ** ((k + 1) / (2 * (k - 1)))


def temperature(la, k):
    return 1 - ((k - 1) * la * la / (k + 1))


def pressure(la, k):
    return temperature(la, k) ** (k / (k - 1))


def density(la, k):
    return temperature(la, k) ** (1 / (k - 1))


def impulse(la, k):
    return (1 + la * la) * density(la, k)


def mass_flow(la, k):
    return la * density(la, k) * ((k + 1) / 2) ** (1 / (k - 1))


def pressure_native(pa, pc):
    return pa / pc


def temperature_native(ta, tc):
    return ta / tc


def mass_flow_native(f_cr, f_a):
    return f_cr / f_a


def pressure_equation(la, k, pa, pc):
    return pressure(la, k) - pressure_native(pa, pc)


def mass_flow_equation(la, k, f_cr, f_a):
    return mass_flow(la, k) - mass_flow_native(f_cr, f_a)


def find_la_p(k, pa, pc):
    return fsolve(pressure_equation, 2, (k, pa, pc))[0]


def find_la_q(k, f_cr, f_a):
    return fsolve(mass_flow_equation, 2, (k, f_cr, f_a))[0]


if __name__ == "__main__":
    print(a_gdf(1.19))  # find A(k)
    print(pressure(2.43, 1.18))  # find pi(lambda, k)
    print(find_la_q(1.18, 1, 100))
