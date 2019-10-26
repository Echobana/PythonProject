import gdf_definitions as fdf


def set_specific_impulse(tor, fuel):
    la = fdf.find_la_p(fuel.k, tor.p_a, tor.p_c)
    return fuel.set_beta() * (fdf.impulse(la, fuel.k) - tor.p_h / tor.p_c) / fdf.mass_flow(la, fuel.k)


def set_specific_impulseq(tor, fuel):
    la = fdf.find_la_q(fuel.k, 1, tor.f_a)
    return fuel.set_beta() * (fdf.impulse(la, fuel.k) - tor.p_h / tor.p_c) / fdf.mass_flow(la, fuel.k)


if __name__ == "__main__":
    pass
