import txt_handler
import pandas as pd


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


if __name__ == '__main__':
    path = r"F:/Elizabeth/FuelData/TxtFiles"
    test_dict = txt_handler.find_data(path)

    textf_creator(test_dict)
    xlsx_creator(test_dict)
