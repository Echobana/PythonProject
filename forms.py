from fuel import FuelDataGround
from fuel import FuelData
from tor import TORA
from tor import TOR
import charachteristics as cta
from resf import RESF
import db_handler


# one single-channel checkerboard with flat ends
class OSCCWFE(RESF):
    def __init__(self, fuel, tor):
        super().__init__(tor, fuel)


# channel gap
class CG(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)


# end
class E(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)


# multicheckers
class MC(RESF):
    def __init__(self, tor, fuel):
        super().__init__(tor, fuel)


if __name__ == "__main__":
    fd_dict = db_handler.db_creator_ground(
        r'F:\Elizabeth\FuelData\data_ground_1.xlsx')  # indata path is changed, ask RD-N1
    tor = TORA(1e6, 55, 7e6, 0, 100, 100)