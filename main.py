from tor import TORA
import db_handler
import txt_handler
import matplotlib.pyplot as plt
from resf import RESF
import forms


def plot_bar(x, y, y_title=''):
    fig_def, ax_def = plt.subplots()
    ax_def.bar(x, y, color='#4B0082', align='center')
    ax_def.set_ylabel(y_title)
    plt.xticks(rotation=90)


if __name__ == "__main__":
    tor = TORA(1e6, 55, 7e6, 0, 100, 100)

    # txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    # fuel_data_dictionary = txt_handler.find_data(txt_data_path)
    # db_handler.xlsx_creator(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # # integrating other data to excel file manually
    # fd_dict = db_handler.db_creator(r'F:\Elizabeth\FuelData\data.xlsx')  # indata path is changed, ask RD-N1
    #
    # txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    # fuel_data_dictionary = txt_handler.find_data_ground(txt_data_path)
    # db_handler.xlsx_creator_ground(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # # integrating other data to excel file manually
    # fd_dict = db_handler.db_creator_ground(
    #     r'F:\Elizabeth\FuelData\data_ground_1.xlsx')  # indata path is changed, ask RD-N1
    #
    # fig, ax = plt.subplots()
    # x_data, y_data = [], []
    # for k, v in fd_dict.items():
    #     x_data.append(k)
    #     y_data.append(v.i_sp)
    # ax.bar(x_data, y_data, color="#00FF7F")
    # ax.set_ylabel("Удельный импульс, $м/c$")
    #
    # cg = dict()
    # for k, v in fd_dict.items():
    #     cg.setdefault(k, forms.CG(tor, v))
    #
    # fig, ax = plt.subplots()
    # xm_data, ym_data = [], []
    # for k, v in cg.items():
    #     xm_data.append(k)
    #     ym_data.append(v.d_out)
    # barlist = plt.bar(xm_data, ym_data, color="#FF1493")
    # barlist[0].set_color('red')
    # barlist[1].set_color('orange')
    # barlist[2].set_color('yellow')
    # barlist[3].set_color('green')
    # barlist[4].set_color('blue')
    # barlist[5].set_color('purple')
    # ax.set_ylabel("Диаметр наружный, $м/c$")

    txt_data_path = r'F:\Elizabeth\FuelData\TxtFiles'
    fuel_data_dictionary = txt_handler.find_data_ground_m(txt_data_path)
    db_handler.xlsx_creator_ground_m(fuel_data_dictionary)  # pay attention to db_handler.xlsx_creator outpath
    # integrating other data to excel file manually
    fd_dict = db_handler.db_creator_ground_m(
        r'F:\Elizabeth\FuelData\data_ground_2.xlsx')  # indata path is changed, ask RD-N1

    fuels, isp_data, z_data = [], [], []
    for k, v in fd_dict.items():
        fuels.append(k)
        isp_data.append(v.i_sp)
        z_data.append(v.z)

    plot_bar(fuels, isp_data, 'Удельный импульс')
    plot_bar(fuels, z_data, 'Содержание к-фазы')

    cg = dict()
    osccwfe = dict()
    e = dict()
    mc = dict()

    for k, v in fd_dict.items():
        cg.setdefault(k, forms.CG(tor, v))
        e.setdefault(k, forms.E(tor, v))
        osccwfe.setdefault(k, forms.OSCCWFE(tor, v))
        mc.setdefault(k, forms.MC(tor, v, 7))

    ym_data = []
    for v in cg.values():
        ym_data.append(v.d_out)
    plot_bar(fuels, ym_data, 'Наружный диаметр')
    # barlist = plt.bar(xm_data, ym_data, color="#FF1493")
    # barlist[0].set_color('red')
    # barlist[1].set_color('orange')
    # barlist[2].set_color('yellow')
    # barlist[3].set_color('green')
    # barlist[4].set_color('blue')
    # barlist[5].set_color('purple')
    # ax.set_ylabel("Диаметр наружный, $м/c$")
    # plt.xticks(rotation=90)

    plt.show()
