import math
from datetime import datetime

import pyotp
from PySide6.QtCore import Signal, QObject, QTimer
from PySide6.QtWidgets import QWidget

from src.controller.KeePassHandler import KeePassHandler


class OTPController(QObject):
    otp_changed = Signal(str)
    time_remaining_changed = Signal(int)

    def __init__(self, keepass_controller: KeePassHandler, keepass_entry: str):
        super().__init__()
        self.uri = keepass_controller.url(keepass_entry)

        self.totp = pyotp.parse_uri(self.uri)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(lambda: self.time_remaining)
        self.update_timer.setInterval(1000)

    @property
    def interval(self) -> int:
        return int(self.totp.interval)

    @property
    def otp(self) -> str:
        return str(self.totp.now())

    @property
    def name(self) -> str:
        return self.totp.name

    @property
    def time_remaining(self) -> float:
        to = float(round(self.interval - datetime.now().timestamp() % self.interval))
        if to <= 0:
            self.otp_changed.emit(self.otp)
        self.time_remaining_changed.emit(to)
        return to


