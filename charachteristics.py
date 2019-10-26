import gdf_definitions as fdf
from fuel import FuelData
from engine import EngineData


def specific_impulse(engine, cfuel):
    la = fdf.find_la_p(cfuel.k, engine.p_a, engine.p_c)
    return cfuel.set_beta() * (fdf.impulse(la, cfuel.k) - engine.p_h / engine.p_c) / fdf.mass_flow(la, cfuel.k)


if __name__ == "__main__":
    pass
