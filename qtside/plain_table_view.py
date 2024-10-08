#  plain_table_view.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QTableView, QFrame


class PlainTableView(QTableView):
    enter_key_pressed = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # 스크롤바는 필요할 때만 보여
        self.setFrameStyle(QFrame.Shape.NoFrame)    # 프레임 없어
        self.setWordWrap(False)                     # 워드랩 끄기
        self.setAlternatingRowColors(True)          # 지브라 칼라
        self.setShowGrid(False)                     # 본문 그리드
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)      # 한줄 전체 선택
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)         # 하나만 선택(다중선택 금지)
        self.setTabKeyNavigation(False)             # 탭 키 탐색 끄기

    # OVERRIDE
    def keyPressEvent(self, event: QKeyEvent):
        current_index = self.currentIndex()
        if current_index.isValid():
            if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                # Key_Return(엔터키), Key_Enter(숫자키패드)
                self.enter_key_pressed.emit(current_index)
                return
        QTableView.keyPressEvent(self, event)


if __name__ == '__main__':
    from PySide6.QtCore import QSize
    from PySide6.QtWidgets import QApplication, QHeaderView
    from mock import *
    from plain_table_model import PlainTableModel, PlainTableItem
    app = QApplication()
    window = MockWindow()
    datasource = PlainTableModel(
        ["TITLE", "DESCRIPTION"],
        []
    )
    datasource.size_hint = QSize(100, 40)
    datasource.reset_sheet([
        PlainTableItem(text=("Hello", "HHHHH")),
        PlainTableItem(text=("World", "WWWWW")),
        PlainTableItem(text=("Haha", "AAAAA")),
        PlainTableItem(text=("Hoho", "OOOOO")),
    ])
    tableview = PlainTableView()
    tableview.setModel(datasource)
    tableview.verticalHeader().setVisible(False)  # 세로 헤더 안 보이게
    tableview.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)  # 고정
    tableview.verticalHeader().setDefaultSectionSize(40)  # 줄높이
    tableview.horizontalHeader().setSectionsClickable(False)  # 헤더 클릭 선택 끄기
    tableview.setModel(datasource)
    tableview.setColumnWidth(0, 100)  # 0번 인덱스 고정 크기
    tableview.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # 나머지 확장
    def list_item_selected(index):
        print("-> Item:", index.data(Qt.ItemDataRole.UserRole))
    tableview.doubleClicked.connect(list_item_selected)
    tableview.enter_key_pressed.connect(list_item_selected)

    window.central_widget_layout.addWidget(tableview)
    window.show()
    app.exec()