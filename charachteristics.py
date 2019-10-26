import gdf_definitions as fdf


def set_specific_impulse(engine, fuel):
    la = fdf.find_la_p(fuel.k, engine.p_a, engine.p_c)
    return fuel.set_beta() * (fdf.impulse(la, fuel.k) - engine.p_h / engine.p_c) / fdf.mass_flow(la, fuel.k)

def set_specific_impulseq(engine, fuel):
    la = fdf.find_la_q(fuel.k, 1, engine.f_a)
    return fuel.set_beta() * (fdf.impulse(la, fuel.k) - engine.p_h / engine.p_c) / fdf.mass_flow(la, fuel.k)

if __name__ == "__main__":
    pass
