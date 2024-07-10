import sys
from typing import Callable, Iterable, Dict
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon
from units.ui import Ui_Form  # Ganti dengan nama modul yang sesuai
from qt_material import apply_stylesheet
from units.rand_string import RandString

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Mengatur ikon aplikasi
        self.setWindowIcon(QIcon('assets/kunci.png'))  

        # inisialisasi untuk menyimpan nilai dari slider
        self.nilai: int = 0

        # inisialisai dict untuk menyimpan nilai bool
        self.data: Dict[str, bool] = {
            'checkBox': False,
            'checkBox_2': False,
            'checkBox_3': False,
            'checkBox_4': False,
        }
        
        # Inisialisasi dictionary untuk menyimpan checkBox
        self.check_boxes: Dict[str, bool] = {
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

        #  atur baris edit hanya baca
        self.ui.lineEdit.setReadOnly(True)
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
        # menyimpan data.values
        vv: Iterable[bool] = list(self.data.values())

        # Mendefinisikan tipe data untuk parameter dan nilai kembalian
        baris: Callable[[str, str], None] = lambda p, q: self.ui.lineEdit.setText(RandString(p, q))

        # kode akan berjalan jika self.nilai lebih dari 0
        if self.nilai > 0: 
            baris('campuran' if all(vv) else
                'besar' if vv[0] and not vv[1] and not vv[2] and not vv[3] else
                'kecil' if not vv[0] and vv[1] and not vv[2] and not vv[3] else
                'digit' if not vv[0] and not vv[1] and vv[2] and not vv[3] else
                'tanda_baca' if not vv[0] and not vv[1] and not vv[2] and vv[3] else 
                self.ui.lineEdit.clear(), self.nilai)
        else:
            self.ui.lineEdit.clear()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    apply_stylesheet(app, theme='light_blue.xml')
    sys.exit(app.exec_())
