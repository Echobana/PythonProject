from engine import TORA
import db_handler
import txt_handler
import matplotlib.pyplot as plt
from resf import RESF


def plot_bar(x, y):
    fig, ax = plt.subplots()
    ax.bar(x, y, color='#4B0082', align='center')
    plt.show()


if __name__ == "__main__":
    engine = TORA(1e6, 55, 7e6, 0, 100)

    txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    fuel_data_dictionary = txt_handler.find_data(txt_data_path)
    db_handler.xlsx_creator(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # integrating other data to excel file manually
    fd_dict = db_handler.db_creator(r'F:\Elizabeth\FuelData\data.xlsx')  # indata path is changed, ask RD-N1

    txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    fuel_data_dictionary = txt_handler.find_data_ground(txt_data_path)
    db_handler.xlsx_creator_ground(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # integrating other data to excel file manually
    fd_dict = db_handler.db_creator_ground(
        r'F:\Elizabeth\FuelData\data_ground.xlsx')  # indata path is changed, ask RD-N1

    x_data, y_data = [], []
    for k, v in fd_dict.items():
        x_data.append(k)
        y_data.append(v.i_sp)

    plot_bar(x_data, y_data)

