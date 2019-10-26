from tor import TORA
from resf import RESF
import db_handler


# one single-channel checkerboard with flat ends
class OSCCWFE(RESF):
    def __init__(self, fuel, tor):
        super().__init__(tor, fuel)

    def set_din(self):
        pass

    def set_dout(self):
        pass

    def set_length(self):
        pass


# channel gap
class CG(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)

    def set_din(self):
        pass

    def set_dout(self):
        pass

    def set_length(self):
        pass

    def set_gap_lenght(self):
        pass

    def set_channel_length(self):
        pass

    def set_gap_width(self):
        pass


# end
class E(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)

    def set_length(self):
        pass

    def set_dout(self):
        pass


# multicheckers
class MC(RESF):
    def __init__(self, tor, fuel, n):
        super().__init__(tor, fuel)
        self.amount = n

    def set_din(self):
        pass

    def set_dout(self):
        pass

    def set_length(self):
        pass


if __name__ == "__main__":
    fd_dict = db_handler.db_creator_ground(
        r'F:\Elizabeth\FuelData\data_ground_1.xlsx')  # indata path is changed, ask RD-N1
    tor = TORA(1e6, 55, 7e6, 0, 100, 100)

    x = fd_dict["AGC"]
    x = RESF(tor, x)
    print(x.u)
