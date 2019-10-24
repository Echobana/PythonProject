class EngineData(object):
    def __init__(self, P, t_w, p_c, p_h, p_a, kappa):
        self.p_c = p_c
        self.P = P
        self.t_w = t_w
        self.p_h = p_h
        self.p_a = p_a
        self.kappa = kappa


class MaterialData(object):
    def __init__(self, sigma_stretch, density):
        self.sigma_stretch = sigma_stretch
        self.density = density


if __name__ == "__main__":
    pass
