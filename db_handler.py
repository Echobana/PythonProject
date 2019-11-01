import pandas as pd
import numpy as np
from fuel import FuelData
from fuel import FuelDataGround
from fuel import FuelDataSol


# Excel file format:
# fuel name
# temperature in combustion chamber
# combustion speed at p = 1 atm
# index in the equation of the law of combustion
# fuel density
# combustion product's molecular mass
# heat capacity ratio


def textf_creator(dictionary):
    f = open('data.txt', 'w')
    for k, v in dictionary.items():
        f.write(str(k) + '\t')
        for parameter in v:
            f.write(str(parameter) + '\t')
        f.write('\n')
    f.close()


def xlsx_creator(dictionary):
    df = pd.DataFrame(dictionary).sort_index(axis=1)

    res = pd.concat([df.iloc[:1],
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     df.iloc[1:]
                     ],
                    ignore_index=True)
    res.to_excel("data.xlsx", index=False)


def xlsx_creator_ground(dictionary):
    df = pd.DataFrame(dictionary).sort_index(axis=1)

    res = pd.concat([df.iloc[:1],
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     df.iloc[1:]
                     ],
                    ignore_index=True)
    res.to_excel("data_ground.xlsx", index=False)


def xlsx_creator_ground_m(dictionary):
    df = pd.DataFrame(dictionary).sort_index(axis=1)

    res = pd.concat([df.iloc[:1],
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     df.iloc[1:]
                     ],
                    ignore_index=True)
    res.to_excel("data_ground_2.xlsx", index=False)


def db_creator(path):
    df = pd.read_excel(path, header=None)
    df = np.array(df).T
    fuel_dict = dict()
    for i in range(len(df)):
        fuel_dict.setdefault(df[i][0], FuelData(*df[i][1:]))
    return fuel_dict


def db_creator_ground(path):
    df = pd.read_excel(path, header=None)
    df = np.array(df).T
    fuel_dict = dict()
    for i in range(len(df)):
        fuel_dict.setdefault(df[i][0], FuelDataGround(*df[i][1:]))
    return fuel_dict


def db_creator_ground_m(path):
    df = pd.read_excel(path, header=None)
    df = np.array(df).T
    fuel_dict = dict()
    for i in range(len(df)):
        fuel_dict.setdefault(df[i][0], FuelDataSol(*df[i][1:]))
    return fuel_dict


if __name__ == '__main__':
    pass
