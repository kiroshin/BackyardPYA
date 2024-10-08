#  icon_button.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


__all__ = ['IconButton']

class IconButton(QPushButton):
    def __init__(self, off_path: str, on_path: str, square=16, parent=None):
        icon = QIcon()
        icon.addFile(off_path, size=QSize(square, square), mode=QIcon.Mode.Normal, state=QIcon.State.Off)
        icon.addFile(on_path, size=QSize(square, square), mode=QIcon.Mode.Normal, state=QIcon.State.On)
        super().__init__(icon=icon, parent=parent)
        self.setIconSize(QSize(square, square))
        self.setCheckable(True)
        self.setObjectName("IconButton")
        self.setStyleSheet(r"#IconButton {background-color: none; border: 0px;}")


if __name__ == '__main__':
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QApplication
    from mock import *
    app = QApplication()
    window = MockWindow()
    icon_button1 = IconButton(
        "../assets/material_favorite_24dp_wght400.svg",
        "../assets/material_favorite_24dp_wght400_fill.svg",
        64,
        parent=window
    )
    icon_button2 = IconButton(
        "../assets/material_favorite_24dp_wght400.svg",
        "../assets/material_favorite_24dp_wght400_fill.svg",
        64,
        parent=window
    )
    icon_button2.setStyleSheet(r"#IconButton {background-color: red; border: 0px;}")
    def btn_changed(ison: bool):
        print("-> Button:", ison)
    icon_button1.clicked.connect(btn_changed)
    icon_button2.clicked.connect(btn_changed)
    window.central_widget_layout.addWidget(icon_button1, 0, Qt.AlignmentFlag.AlignCenter)
    window.central_widget_layout.addWidget(icon_button2, 0, Qt.AlignmentFlag.AlignCenter)
    window.show()
    app.exec()

