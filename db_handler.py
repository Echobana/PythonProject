import txt_handler
import openpyxl
import xlrd

if __name__ == '__main__':
    path = r"F:/Elizabeth/FuelData/TxtFiles"
    test_dict = txt_handler.find_data(path)
    print(test_dict)


    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    data_list = list(test_dict.values())
    print(data_list)
    test_dict = {'a': [1, 2], 'b': [2, 3]}

    for columnnum in range(len(test_dict)):
        for rownum in range(len(list(test_dict.values())[0])):
            sheet.cell(row=rownum+2, column=columnnum+1).value = list(test_dict.values())[columnnum][rownum]
    wb.save("sample.xlsx")