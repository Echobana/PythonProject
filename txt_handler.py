import re
import os


def find_data(path):
    files = os.listdir(path)

    data_dict = dict()

    for file in files:
        filename = path + "/" + file
        file_data = open(filename)
        data = file_data.read()
        data_dict.setdefault(file, data)

    # Создание регулярных выражений для поиска температуры, импульса и к-фазы
    t_regex = re.compile(r'T=(\d*\.\d*|\d*)')
    k_regex = re.compile(r'k=(\d*\.\d*)')
    rg_regex = re.compile(r'Rg=(\d*\.\d*)')
    name_regex = re.compile(r'(.*)\.txt')

    regular = dict()

    for k, v in data_dict.items():
        t_mo = t_regex.findall(v)
        k_mo = k_regex.findall(v)
        rg_mo = rg_regex.findall(v)
        name_mo = name_regex.findall(k)
        regular.setdefault(name_mo[0],
                           [float(t_mo[0]),  # temperature
                            8.314 / float(rg_mo[0]),  # molecular mass
                            float(k_mo[0])])  # heat capacity ratio
    return regular


def find_data_ground(path):
    files = os.listdir(path)

    data_dict = dict()

    for file in files:
        filename = path + "/" + file
        file_data = open(filename)
        data = file_data.read()
        data_dict.setdefault(file, data)

    # Создание регулярных выражений для поиска температуры, импульса и к-фазы
    t_regex = re.compile(r'T=(\d*\.\d*|\d*)')
    isp_regex = re.compile(r'Isp=(\d*\.\d*|\d*)')
    k_regex = re.compile(r'k=(\d*\.\d*|\d*)')
    rg_regex = re.compile(r'Rg=(\d*\.\d*|\d*)')
    name_regex = re.compile(r'(.*)\.txt')
    beta_regex = re.compile(r'B=(\d*\.\d*|\d*)')

    regular = dict()

    for k, v in data_dict.items():
        t_mo = t_regex.findall(v)
        isp_mo = isp_regex.findall(v)
        k_mo = k_regex.findall(v)
        rg_mo = rg_regex.findall(v)
        beta_mo = beta_regex.findall(v)
        name_mo = name_regex.findall(k)
        regular.setdefault(name_mo[0],
                           [float(t_mo[0]),  # temperature
                            8.314 / float(rg_mo[0]),  # molecular mass
                            float(k_mo[0]),  # heat capacity ratio
                            float(beta_mo[0]),
                            float(isp_mo[1])])  # specific impulse
    return regular


def find_data_ground_m(path):
    files = os.listdir(path)

    data_dict = dict()

    for file in files:
        filename = path + "/" + file
        file_data = open(filename)
        data = file_data.read()
        data_dict.setdefault(file, data)

    # Создание регулярных выражений для поиска температуры, импульса и к-фазы
    t_regex = re.compile(r'T=(\d*\.\d*|\d*)')
    isp_regex = re.compile(r'Isp=(\d*\.\d*|\d*)')
    k_regex = re.compile(r'k=(\d*\.\d*|\d*)')
    rg_regex = re.compile(r'Rg=(\d*\.\d*|\d*)')
    name_regex = re.compile(r'(.*)\.txt')
    beta_regex = re.compile(r'B=(\d*\.\d*|\d*)')
    z_regex = re.compile(r'z=(\d*\.\d*|\d*)')
    w_regex = re.compile(r'w=(\d*\.\d*|\d*)')
    v_regex = re.compile(r'v=(\d*\.\d*|\d*)')

    regular = dict()

    for k, v in data_dict.items():
        t_mo = t_regex.findall(v)
        isp_mo = isp_regex.findall(v)
        k_mo = k_regex.findall(v)
        rg_mo = rg_regex.findall(v)
        beta_mo = beta_regex.findall(v)
        name_mo = name_regex.findall(k)
        z_mo = z_regex.findall(v)
        w_mo = w_regex.findall(v)
        v_mo = v_regex.findall(v)
        regular.setdefault(name_mo[0],
                           [float(t_mo[0]),  # temperature
                            8.314 / float(rg_mo[0]),  # molecular mass
                            float(k_mo[0]),  # heat capacity ratio
                            float(beta_mo[0]),
                            float(isp_mo[1]),
                            float(z_mo[0]),
                            float(w_mo[1]),
                            float(v_mo[0])])  # specific impulse
    return regular


if __name__ == "__main__":
    pass
