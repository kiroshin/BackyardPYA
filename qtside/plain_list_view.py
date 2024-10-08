#  plain_list_view.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QListView, QFrame


class PlainListView(QListView):
    enter_key_pressed = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setFrameStyle(QFrame.Shape.NoFrame)
        self.setAlternatingRowColors(True)

    # OVERRIDE
    def keyPressEvent(self, event: QKeyEvent):
        current_index = self.currentIndex()
        if current_index.isValid():
            if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                # Key_Return(엔터키), Key_Enter(숫자키패드)
                self.enter_key_pressed.emit(current_index)
                return
        QListView.keyPressEvent(self, event)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from mock import *
    from plain_list_model import PlainListModel, PlainListItem
    app = QApplication()
    window = MockWindow()
    datasource = PlainListModel()
    datasource.size_hint = QSize(100, 40)
    datasource.reset_sheet([
        PlainListItem(text="Hello"),
        PlainListItem(text="World"),
        PlainListItem(text="Haha"),
        PlainListItem(text="Hoho"),
    ])
    listview = PlainListView()
    listview.setModel(datasource)
    def list_item_selected(index):
        print("-> Item:", index.data(Qt.ItemDataRole.UserRole))
    listview.doubleClicked.connect(list_item_selected)
    listview.enter_key_pressed.connect(list_item_selected)
    window.central_widget_layout.addWidget(listview)
    window.show()
    app.exec()

