import sys
from typing import Callable, List, Dict
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon
from units.ui import Ui_Form
from style.karbon import karbon
from units import rand_string_grafis, kombinasi_kamus_elemen_bool, kombinasi_kamus, data_huruf

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assets/kunci.png'))
        self.nilai: int = 0
        self.data: Dict[str, bool] = {
            'checkBox': False,
            'checkBox_2': False,
            'checkBox_3': False,
            'checkBox_4': False}
        self.check_boxes: Dict[str, bool] = {
            'checkBox': self.ui.checkBox,
            'checkBox_2': self.ui.checkBox_2,
            'checkBox_3': self.ui.checkBox_3,
            'checkBox_4': self.ui.checkBox_4}
        for checkbox in self.check_boxes.values():
            checkbox.stateChanged.connect(self.checkbox_state_changed)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_changed)
        self.ui.horizontalSlider.setMinimum(7)
        self.ui.horizontalSlider.setMaximum(15)
        self.ui.lineEdit.setReadOnly(True)
        self.ui.pushButton.clicked.connect(self.saat_ditekan)

    def checkbox_state_changed(self, state):
        sender_checkbox = self.sender()
        checkbox_name = next(name for name, checkbox in self.check_boxes.items() if checkbox == sender_checkbox)
        if checkbox_name:
            checkbox_value = sender_checkbox.isChecked()
            self.data[checkbox_name] = checkbox_value

    def slider_value_changed(self, value):
        self.nilai = value
        self.ui.label_7.setText(str(value)) 

    def saat_ditekan(self):
        vv: List[bool] = list(self.data.values())
        kmus = kombinasi_kamus(data_huruf).keys()
        kmus_bool = kombinasi_kamus_elemen_bool(data_huruf)
        for k in kmus:
            if vv == kmus_bool.get(k):
                self.ui.lineEdit.setText(rand_string_grafis(k, self.nilai))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(karbon)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
