import pathlib
import subprocess
import time

import psutil

from src.controller.KeePassHandler import KeePassHandler
from src.controller.OTPController import OTPController


class VPNClient:
    def __init__(self, install_path):
        self.install_path = pathlib.Path(install_path).absolute()

        self.vpn_client = pathlib.Path(fr"{self.install_path}\vpncli.exe")
        self.ui_client = pathlib.Path(fr"{self.install_path}\UI\csc_ui.exe")

    def parse_error(self):
        pass
    def connect(self, host, username, kph: KeePassHandler, otph: OTPController):
        self.kill_ui()

        command = [self.vpn_client, "-s", "connect", host]

        try:
            process = subprocess.Popen(command,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)

            stdout, stderr = process.communicate(input=f"{username}\n{kph.password}\n{otph.otp}\ny\n")
            print(stdout)
            if stderr:
                print("Error:", stderr)
            else:
                print("VPN connected successfully.")
                process.kill()

        except FileNotFoundError:
            print("VPN client executable not found.")
        except subprocess.CalledProcessError as e:
            print("Error connecting to VPN:", e)

        self.start_ui()

    def kill_ui(self):
        PROCNAME = "csc_ui.exe"

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
                print("Killed!")

    def start_ui(self):
        subprocess.Popen(self.ui_client)

if __name__ == "__main__":
    vpnc = VPNClient("C:\Program Files (x86)\Cisco\Cisco Secure Client")
