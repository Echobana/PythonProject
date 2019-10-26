from engine import A_EngineData
import charachteristics as cta
import db_handler
import txt_handler

if __name__ == "__main__":
    engine = A_EngineData(1e6, 55, 7e6, 0, 100)

    txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    fuel_data_dictionary = txt_handler.find_data(txt_data_path)
    db_handler.xlsx_creator(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # integrating other data to excel file manually
    fd_dict = db_handler.db_creator(r'F:\Elizabeth\FuelData\data.xlsx')  # indata path is changed, ask RD-N1

    for k, v in fd_dict.items():
        print(k, cta.set_specific_impulseq(engine, v))

    txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    fuel_data_dictionary = txt_handler.find_data_ground(txt_data_path)
    db_handler.xlsx_creator_ground(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # integrating other data to excel file manually
    fd_dict = db_handler.db_creator_ground(
        r'F:\Elizabeth\FuelData\data_ground.xlsx')  # indata path is changed, ask RD-N1
    print()
    for k, v in fd_dict.items():
        print(k, v.beta)

