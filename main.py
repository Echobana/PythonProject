from engine import EngineData
from material import MaterialData
from fuel import FuelData
import gdf_definitions as ffd
import txt_handler
import charachteristics as cta
import db_handler
import pandas as pd
import numpy as np
my_fuel = FuelData(2351, 0.7e-3, 0.6, 1600, 23.4e-3, 1.18)
my_engine = EngineData(1000, 3, 12e6, 0.05e6, 0.05e6, 100)

i_sp = cta.specific_impulse(my_engine, my_fuel)

path = r'F:\Elizabeth\FuelData\data.xlsx'
df = pd.read_excel(path, header=None)
df = np.array(df).T

fuel_dict = dict()

for i in range(len(df)):
    fuel_dict.setdefault(df[i][0], FuelData(*df[i][1:]))








