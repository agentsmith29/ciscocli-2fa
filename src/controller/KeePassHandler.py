
from pykeepass import PyKeePass

from src.controller.VPNConfig import KeePassConfig


class KeePassHandler:

    def __init__(self, config: KeePassConfig):
        self.config = config

        self.kp = PyKeePass(self.config.kbx_database.get(), keyfile=self.config.kbx_keyfile.get())

        self.password_retrieved = False

    def password(self, entry):
        return self.kp.find_entries_by_title(entry, first=True).password

    def username(self, entry):
        return self.kp.find_entries_by_title(entry, first=True).username

    def url(self, entry):
        return self.kp.find_entries_by_title(entry, first=True).url


    def get_all_entries(self):
        return self.kp.entries
