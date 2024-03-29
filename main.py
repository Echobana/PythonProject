from tor import TORA
import db_handler
import txt_handler
import matplotlib.pyplot as plt
import forms
import os


def plot_bar(x, y, y_title=''):
    colors = (
    '#FF0000', '#7B68EE', '#00FF00', '#00FFFF', '#FF00FF', '#00FA9A', '#FFD700', '#DA70D6', '#000080', '#00CED1')
    fig_def, ax_def = plt.subplots()
    bar_list = ax_def.bar(x, y, color='pink', align='center')
    for i in range(len(colors)):
        bar_list[i].set_color(colors[i])
    ax_def.set_ylabel(y_title)
    plt.xticks(rotation=30)
    ax_def.grid(ls='--')


def plot_bar_double(x, y1, y2, y_title=''):
    colors = (
    '#FF0000', '#7B68EE', '#00FF00', '#00FFFF', '#FF00FF', '#00FA9A', '#FFD700', '#DA70D6', '#000080', '#00CED1')
    fig_def, (ax_def_left, ax_def_right) = plt.subplots(nrows=2)
    bar_list_left = ax_def_left.bar(x, y1, align='center', label="left")
    bar_list_right = ax_def_right.bar(x, y2, align='center')
    for i in range(len(colors)):
        bar_list_left[i].set_color(colors[i])
        bar_list_right[i].set_color(colors[i])
    ax_def_left.grid(ls="--")
    ax_def_right.grid(ls="--")
    ax_def_left.set_title("Наружный диаметр")
    ax_def_right.set_title("Удлинение")
    fig_def.suptitle(y_title)


if __name__ == "__main__":
    # thrust impulse, time, chamber pressure, atmosphere pressure, f_a, Pobedonostsev criteria
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
    xlsx_data_path = r'F:\Elizabeth\FuelData\data_ground_2.xlsx'  # <---------------------------EDIT HERE

    if os.path.exists(txt_data_path):
        fd_dict = db_handler.db_creator_ground_m(xlsx_data_path)
    else:
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

    fuels = ('AGC', 'ПХА-3М', 'ПХА-4М', 'ПХА-5М', 'ARCADENE 253A', 'CYN', 'Н', 'ПХК-1М', 'ПХН-2М', 'RD2435')
    # plot_bar(fuels, isp_data, 'Удельный импульс')
    # plot_bar(fuels, z_data, 'Содержание к-фазы')

    cgfe = dict()
    osccwfe = dict()
    e = dict()
    mc = dict()
    tfe = dict()

    shapes_tuple = (cgfe, osccwfe, e, mc, tfe)

    for k, v in fd_dict.items():
        cgfe.setdefault(k, forms.CGFE(tor, v))
        e.setdefault(k, forms.E(tor, v))
        osccwfe.setdefault(k, forms.OSCCWFE(tor, v))
        tfe.setdefault(k, forms.TFE(tor, v))
        mc.setdefault(k, forms.MC(tor, v, 7))

    yplot_data_elongation = []
    yplot_data_d = []

    titles = ('Канально-щелевой заряд с плоскими торцами',
              'Одношечный одноканальный заряд с плоскими торцами',
              'Торцевой заряд',
              'Многошашечный заряд',
              'Телескопический заряд'
              )

    for shape in shapes_tuple:
        y = []
        y_elongation = []
        y_d_out = []
        for v in shape.values():
            y_elongation.append(v.length / v.d_out)
            y_d_out.append(v.d_out)
            # y.append(v.fuel_mass)
        yplot_data_elongation.append(y_elongation)
        yplot_data_d.append(y_d_out)

    for i in range(len(yplot_data_elongation)):
        plot_bar(fuels, yplot_data_elongation[i], y_title=titles[i])
    # for i in range(len(yplot_data_rate)):
    #     plot_bar_double(fuels, yplot_data_d[i], yplot_data_rate[i], y_title=titles[i])

    plt.show()
