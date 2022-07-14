from openpyxl import Workbook


class Save_xlsx:  # [[1, 2], [1, 2]]
    def __init__(self, data, path_to_file):
        workbook_for_save = Workbook()
        workbook = workbook_for_save.active
        for count in data:
            workbook.append(count)
        workbook_for_save.save(path_to_file)


class Save_csv:  # [[1, 2], [1, 2]]
    def __init__(self, data,path_to_file):
        new_file_csv = open(path_to_file, 'w')
        for elemment in data:
            print(';'.join(map(str, elemment)), file=new_file_csv)
        new_file_csv.close()


class Save_txt:
    def __init__(self, data, file_name):
        new_file_txt = open(file_name, 'w')
        print(data, file=new_file_txt)
        new_file_txt.close()
