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
    isp_regex = re.compile(r'Isp=(\d*\.\d*|\d*)')
    k_regex = re.compile(r'k=(\d*\.\d*)')
    rg_regex = re.compile(r'Rg=(\d*\.\d*)')
    # z_regex = re.compile(r'z=(\d*\.\d*)')
    name_regex = re.compile(r'(.*)\.txt')

    regular = dict()

    for k, v in data_dict.items():
        t_mo = t_regex.findall(v)
        isp_mo = isp_regex.findall(v)
        k_mo = k_regex.findall(v)
        rg_mo = rg_regex.findall(v)
        # z_mo = z_regex.findall(v)
        name_mo = name_regex.findall(k)
        regular.setdefault(name_mo[0],
                           [float(t_mo[0]),  # temperature
                            float(rg_mo[0]),  # R
                            float(isp_mo[1]),  # specific_impulse
                            float(k_mo[0])])  # heat capacity ratio
    return regular


def textf_creator(dict):
    f = open('data.txt', 'w')
    for k, v in test_dict.items():
        f.write(str(k) + '\t')
        for parameter in v:
            f.write(str(parameter) + '\t')
        f.write('\n')
    f.close()


if __name__ == "__main__":
    path = r"F:/Elizabeth/FuelData/TxtFiles"
    test_dict = find_data(path)
    print(test_dict)
    textf_creator(test_dict)
