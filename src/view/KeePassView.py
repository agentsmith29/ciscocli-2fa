from PySide6.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton

from src.controller.KeePassHandler import KeePassHandler


class KeePassView(QWidget):

    def __init__(self, controller: KeePassHandler):
        super().__init__()
        self.controller = controller
        self.layout = QGridLayout()

        self.kbx_database = self.controller.config.kbx_database.view.ui_field()
        self.layout.addWidget(self.kbx_database, 0, 0, 1, 3)

        self.kbx_keyfile = self.controller.config.kbx_keyfile.view.ui_field()
        self.layout.addWidget(self.kbx_keyfile, 1, 0, 1, 3)

        self.password_label = QLabel("Password")
        self.password_reveal = QPushButton("Reveal")
        self.password_textfield = QLineEdit()
        self.on_password_reveal_up()
        self.password_reveal.pressed.connect(self.on_password_reveal_down)
        self.password_reveal.released.connect(self.on_password_reveal_up)

        #self.entry_label = QLabel("Entry")
        #self.entry_textfield = QLineEdit(self.controller.config.kbx_entry.get())


        self.layout.addWidget(self.password_label, 2, 0, 1, 1)
        self.layout.addWidget(self.password_textfield, 2, 1, 1, 1)
        self.layout.addWidget(self.password_reveal, 2, 2, 1, 1)
        #self.layout.addWidget(self.entry_label, 3, 0, 1, 3)
        #self.layout.addWidget(self.entry_textfield, 3, 1, 1, 1)

        self.setLayout(self.layout)

    def on_password_reveal_down(self):
        self.password_textfield.setEchoMode(QLineEdit.EchoMode.Normal)

    def on_password_reveal_up(self):
        self.password_textfield.setEchoMode(QLineEdit.EchoMode.Password)