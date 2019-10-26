from engine import EngineData
from material import MaterialData
from fuel import FuelData
import gdf_definitions as ffd
import charachteristics as cta
import db_handler
import txt_handler

txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
fuel_data_dictionary = txt_handler.find_data(txt_data_path)
db_handler.xlsx_creator(fuel_data_dictionary)
# integrating other data to excel file
fd_dict = db_handler.db_creator(r'F:\Elizabeth\FuelData\data.xlsx')

