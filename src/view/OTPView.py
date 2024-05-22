from PySide6.QtWidgets import QLabel, QWidget, QLineEdit, QGroupBox, QVBoxLayout, QGridLayout

from src.controller.OTPController import OTPController
from src.view.CBar import CPBar


class OTPView(QWidget):
    def __init__(self, controller: OTPController):
        super().__init__()
        self.controller = controller



        #self.groupbox1 = QGroupBox("One Time Password")

        self.glayout = QGridLayout()
        self._otp_uri = QLineEdit(self.controller.uri)
        self.glayout.addWidget(self._otp_uri, 0, 0, 1, 1)

        self.otp_token_name = QLabel(str(self.controller.name))
        self.otp_textfield = QLineEdit(str(self.controller.otp))
        self.otp_time_remaining = QLineEdit(str(self.controller.time_remaining))

        self.glayout.addWidget(self.otp_token_name, 1, 0, 1, 1)
        self.glayout.addWidget(self.otp_textfield, 2, 0, 1, 1)
       # self.glayout.addWidget(self.otp_time_remaining, 3, 0, 1, 1)

        self.p = CPBar(self)
        self.glayout.addWidget(self.p, 0, 2, 3, 1)

        self.setLayout(self.glayout)

        self.controller.otp_changed.connect(self._on_otp_changed)
        self.controller.time_remaining_changed.connect(self._on_time_remaining_changed)
        self.controller.update_timer.start()


    def _on_otp_changed(self, otp):
        self.otp_textfield.setText(str(otp))
    def _on_time_remaining_changed(self, tr):
        self.otp_time_remaining.setText(str(tr))
        self.p.upd2(tr, self.controller.interval)
