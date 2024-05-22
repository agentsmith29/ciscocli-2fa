from PySide6 import QtWidgets

from src.controller.VPNController import VPNController
from src.view.VPNView import VPNView


#


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    vpn_controller = VPNController()
    vpn_view = VPNView(vpn_controller)
    vpn_view.show()
    app.exec()