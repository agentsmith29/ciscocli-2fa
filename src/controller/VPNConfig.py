import pathlib

import confighandler as cfg
from pathlib import Path


class VPNConfig(cfg.ConfigNode):

    def __init__(self, enable_log=True) -> None:
        # Call the base class (important!)
        super().__init__()

        self.host: cfg.Field[str] = cfg.Field("vpn.tugraz.at",
                                               "VPN Hostname",
                                               description="The VPN Hostname or IP Address")

        self.vpn_install_folder = cfg.Field(
            Path("C:\Program Files (x86)\Cisco\Cisco Secure Client"),
            friendly_name="Install Folder",
            description="The VPN Install Folder")


        # Add an entry with the name "Eduroam Netzzugangskennwort" and addd your VPN username and password.
        self.kbx_entry_vpn_credentials: cfg.Field[str] = cfg.Field("VPN Credentials")

        # Add an Entry with the given name (TU Graz OTP Link) and add the oauth url as the field url
        self.kbx_entry_otp_link: cfg.Field[str] = cfg.Field("OTP Url")

        self.keepass_config = KeePassConfig()

        # Don't forget to register the fields (important!)
        self.register()

class KeePassConfig(cfg.ConfigNode):

    def __init__(self, enable_log=True) -> None:
        # Call the base class (important!)
        super().__init__()
        self.kbx_database: cfg.Field = cfg.Field(
            Path(r"Link/to/Database.kdbx"),
            friendly_name="KeePass Database File (kbx)",
            description="The KP-Database File")

        self.kbx_keyfile: cfg.Field = cfg.Field(
            Path(r"Link/to/DatabaseKeys.keyx"),
            friendly_name="KeePass Key File (keyx)",
            description="The KP-Database Key file for opening")


        # Don't forget to register the fields (important!)
        self.register()

