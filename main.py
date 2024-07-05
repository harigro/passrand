import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon
from ui_apps.ui import Ui_Form  # Ganti dengan nama modul yang sesuai
from qt_material import apply_stylesheet
from rand_string.rand_string import RandString

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Mengatur ikon aplikasi
        self.setWindowIcon(QIcon('assets/kunci.png'))  

        # inisialisasi untuk menyimpan nilai dari slider
        self.nilai = 0

        # Inisialisasi dictionary untuk menyimpan checkBox
        self.data = {}
        self.check_boxes = {
            'checkBox': self.ui.checkBox,
            'checkBox_2': self.ui.checkBox_2,
            'checkBox_3': self.ui.checkBox_3,
            'checkBox_4': self.ui.checkBox_4,
        }

        # Hubungkan sinyal stateChanged dari semua checkBox ke metode self.checkbox_state_changed
        for checkbox in self.check_boxes.values():
            checkbox.stateChanged.connect(self.checkbox_state_changed)

        # Hubungkan sinyal valueChanged dari horizontalSlider ke metode self.slider_value_changed
        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_changed)

        # Atur nilai minimum dan maksimum untuk horizontalSlider
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(12)

        # Hubungkan sinyal clicked dari pushButton ke metode self.saat_ditekan
        self.ui.pushButton.clicked.connect(self.saat_ditekan)

    def checkbox_state_changed(self, state):
        # Mendapatkan checkbox yang menyebabkan perubahan
        sender_checkbox = self.sender()

        # Mendapatkan nama checkbox
        checkbox_name = next(name for name, checkbox in self.check_boxes.items() if checkbox == sender_checkbox)

        if checkbox_name:
            # Mendapatkan nilai aktual checkbox
            checkbox_value = sender_checkbox.isChecked()
            self.data[checkbox_name] = checkbox_value

    def slider_value_changed(self, value):
        # Mendapatkan nilai aktual dari horizontalSlider
        self.nilai = value

    def saat_ditekan(self):
        # print("Berjalan dengan baik")
        if len(self.data) > 0 and self.nilai > 0:
            for i, v in self.data.items():
                if i == 'checkBox' and v == True:
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setText(RandString("uppercase", self.nilai))
                if i == 'checkBox_2' and v == True:
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setText(RandString("lowercase", self.nilai))
                if i == 'checkBox_3' and v == True:
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setText(RandString("digits", self.nilai))
                if i == 'checkBox_4' and v == True:
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setText(RandString("ascii", self.nilai))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    apply_stylesheet(app, theme='dark_blue.xml')
    sys.exit(app.exec_())
