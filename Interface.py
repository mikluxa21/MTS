from desine import  Ui_MainWindow
from save import Save_csv, Save_txt, Save_xlsx

from PySide6.QtWidgets import QMainWindow, QFileDialog

from normal_form import Normal

class Inter(QMainWindow):
    def __init__(self):
        super(Inter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connect PushBatton
        self.ui.pushButton.clicked.connect(lambda: self.Download())

        #connect Save
        self.ui.Save.triggered.connect(lambda: self.Save_as('.txt'))
        self.ui.Save_as_txt.triggered.connect(lambda: self.Save_as('.txt'))
        self.ui.Save_as_csv.triggered.connect(lambda: self.Save_as('.csv'))
        self.ui.Save_as_exel.triggered.connect(lambda: self.Save_as('.xlsx'))

    #functions:
    def Download(self)->None:
        self.ui.lineEdit.setText('HellowWorld')

    def Save_as(self, extension: str)->None:
        file = str(QFileDialog.getSaveFileName(self, "Выберите папку"))[2:-19]
        if extension =='.txt':
            Save_txt(file, file + '.txt')
        elif extension == '.csv':
            dict_for_test = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}  #delete
            Save_csv(Normal().For_save(dict_for_test), file + '.csv')
        elif extension == '.xlsx':
            dict_for_test = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}  #delete
            Save_xlsx(Normal().For_save(dict_for_test), file + '.xlsx')
