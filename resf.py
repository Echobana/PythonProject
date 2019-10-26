import charachteristics as cta


class RESF(object):
    def __init__(self, engine, fuel):
        self.isp = cta.set_specific_impulse()