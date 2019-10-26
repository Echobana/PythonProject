import txt_handler
import pandas as pd

"""
.xlsx format:
fuel name
temperature in combustion chamber
combustion speed at p = 1 atm
index in the equation of the law of combustion
fuel denisty
сombustion product's molecular mass
heat capacity ratio
"""

if __name__ == '__main__':
    path = r"F:/Elizabeth/FuelData/TxtFiles"
    test_dict = txt_handler.find_data(path)

    df = pd.DataFrame(test_dict).sort_index(axis=1)

    res = pd.concat([df.iloc[:1],
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     pd.DataFrame([[""] * len(df.columns)], columns=df.columns),
                     df.iloc[1:]
                     ],
                    ignore_index=True)
    res.to_excel("data.xlsx", index=False)



