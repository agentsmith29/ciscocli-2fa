from src.controller.KeePassHandler import KeePassHandler
from src.controller.OTPController import OTPController
from src.controller.VPNClient import VPNClient
from src.controller.VPNConfig import VPNConfig
from src.view.OTPView import OTPView


class VPNController():
    def __init__(self):
        self.config = VPNConfig()
        self.config.autosave(True)



        #self._kbx_database = r"G:\Meine Ablage\Dokumente\Gesicherte Objekte\KP\Database.kdbx"
        #self._kbx_keyfile = r"C:\Users\myjustice\KBX Files\Database.keyx"
        #self._kbx_entry = "Eduroam Netzzugangskennwort"
        self.keepass_controller = KeePassHandler(self.config.keepass_config)

        self.username = self.keepass_controller.username(self.config.kbx_entry_vpn_credentials)
        self.host = "vpn.tugraz.at"

        self.otp_controller = OTPController(self.keepass_controller, self.config.kbx_entry_otp_link.get())



        self.vpn_client = VPNClient("C:\Program Files (x86)\Cisco\Cisco Secure Client")

    def connect(self):
        self.vpn_client.connect(
        self.host, self.username,
        self.keepass_controller,
        self.otp_controller
        )