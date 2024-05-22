from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QGroupBox, QLineEdit, QPushButton

from src.controller.VPNController import VPNController
from src.view.KeePassView import KeePassView
from src.view.OTPView import OTPView


class VPNView(QMainWindow):
    def __init__(self, vpn_controller: VPNController):
        super().__init__()
        self.vpn_controller = vpn_controller



        self.otp_view = OTPView(self.vpn_controller.otp_controller)
        self.keepass_view = KeePassView(self.vpn_controller.keepass_controller)



        self.setWindowTitle("VPN Configuration")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.groupbox1 = QGroupBox("Group Box 1")
        self.layout.addWidget(self.groupbox1)

        self.groupbox1_layout = QVBoxLayout()
        self.groupbox1.setLayout(self.groupbox1_layout)


        self._vpn_host = self.vpn_controller.config.host.view.ui_field()
        self.groupbox1_layout.addWidget(self._vpn_host)

        self._username = QLineEdit(self.vpn_controller.username)
        self.groupbox1_layout.addWidget(self._username)

        self.groupbox_otp = QGroupBox("One Time Password")
        self.groupbox_otp_layout = QVBoxLayout()
        self.groupbox_otp.setLayout(self.groupbox_otp_layout)
        self.groupbox_otp_layout.addWidget(self.otp_view)


        self.groupbox_keepass = QGroupBox("KeePass Client")
        self.groupbox_keepass_layout = QVBoxLayout()
        self.groupbox_keepass.setLayout(self.groupbox_keepass_layout)
        self.groupbox_keepass_layout.addWidget(self.keepass_view)

        self.layout.addWidget(self.groupbox_otp)
        self.layout.addWidget(self.groupbox_keepass)




        self.groupbox2 = QGroupBox("Group Box 2")
        self.layout.addWidget(self.groupbox2)

        self.groupbox2_layout = QVBoxLayout()
        self.groupbox2.setLayout(self.groupbox2_layout)

        self._vpn_install_folder = self.vpn_controller.config.vpn_install_folder.view.ui_field()
        self.groupbox1_layout.addWidget(self._vpn_install_folder)


        #self.db_label = QLabel("KeePass Database")
        #self.db_textfield = QLineEdit()
        #self.groupbox2_layout.addWidget(self.db_label)
        #self.groupbox2_layout.addWidget(self.db_textfield)





        #self.keyfile_label = QLabel("KeePass Key File")
        #self.keyfile_textfield = QLineEdit()
        #self.groupbox2_layout.addWidget(self.keyfile_label)
        #self.groupbox2_layout.addWidget(self.keyfile_textfield)


        self.ok_button = QPushButton("Connect now!")
        self.ok_button.clicked.connect(self.on_ok_clicked)

        self.abort_button = QPushButton("Abort")
        self.abort_button.clicked.connect(self.on_abort_clicked)

        self.layout.addWidget(self.ok_button)
        self.layout.addWidget(self.abort_button)


    def on_ok_clicked(self):
        # Placeholder function for the Ok button
        print("Ok button clicked")
        self.vpn_controller.connect()

    def on_abort_clicked(self):
        # Placeholder function for the Abort button
        print("Abort button clicked")
