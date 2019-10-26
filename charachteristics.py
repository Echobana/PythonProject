import gdf_definitions as ffd
from fuel import FuelData
from engine import EngineData


def specific_impulse(engine, cfuel):
    la = ffd.find_la_p(cfuel.k, engine.p_a, engine.p_c)
    return cfuel.set_beta() * (ffd.impulse(la, cfuel.k) - engine.p_h / engine.p_c) / ffd.mass_flow(la, cfuel.k)

if __name__ == "__main__":
    pass
