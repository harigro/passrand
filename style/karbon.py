# memperbaiki checkbox dan slider
karbon = """
/*-----QWidget-----*/
QWidget {
	background-color: #dadada;
}

/*-----QLabel-----*/
QLabel {
    font-size: 15px;
	color: #393939;
    font-weight: 500;
}

QLabel#label {
    margin-bottom: 10px;
    font-size: 25px;
    color: #303030;
    font-weight: bold;
}

QLabel#label_7 {
    margin: 2px;
}

/*-----QLineEdit-----*/
QLineEdit {
    padding: 10px;
    font-size: 15px;
    font-weight: 500;
    border-style: none;
    border-bottom: 2px solid #99667f;
    color: #6c0681;
}

/*-----QCheckBox-----*/
QCheckBox {
	background-color: transparent;
    color: lightgray;
	border: none;

}

QCheckBox::indicator {
    background-color: #c1c1c1;
    border: 1px solid darkgray;
    width: 12px;
    height: 12px;

}

QCheckBox::indicator:checked {
	background-color: #b78620;
    border: 1px solid #3a546e;

}

QCheckBox::indicator:unchecked:hover {
	border: 1px solid #b78620; 

}

/*-----QSlider-----*/
QSlider::groove:horizontal {
	background-color: transparent;
	height: 3px;
}

QSlider::sub-page:horizontal {
	background-color: #b78620;
}

QSlider::add-page:horizontal {
	background-color: #434343;
}

QSlider::handle:horizontal {
	background-color: #b78620;
	width: 14px;
	margin-top: -6px;
	margin-bottom: -6px;
	border-radius: 6px;
}

QSlider::handle:horizontal:hover {
	background-color: #d89e25;
	border-radius: 6px;
}

/*-----QPushButton-----*/
QPushButton {
	background-color: #22cba6;
	color: #303030;
	border-radius: 3px;
    border: 2px solid #082d25;
	padding: 10px;
    font-size: 15px;
}

QPushButton::hover {
	background-color: #20bf9a;
	border: 2px solid #082d25;

}

QPushButton::pressed{
	background-color: #1eb390;
}
"""