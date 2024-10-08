#  mock.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from PySide6.QtGui import QAction, QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QToolBar, QVBoxLayout

__all__ = ['MockWindow', 'MockCell']


class MockWindow(QMainWindow):
    def __init__(self, w=400, h=400):
        super().__init__()
        self.setMinimumSize(300, 300)
        self.resize(w, h)

        toolbar = QToolBar()
        toolbar.setMovable(False)  # 툴바 뜯어내서 움직이는 것 여부(기본값 True)
        self.addToolBar(toolbar)

        alpha = QAction("alpha", self)
        toolbar.addAction(alpha)
        self.alpha_action = alpha
        # self.alpha_action.triggered.connect(...)

        beta = QAction("beta", self)
        toolbar.addAction(beta)
        self.beta_action = beta

        gamma = QAction("gamma", self)
        toolbar.addAction(gamma)
        self.gamma_action = gamma

        delta = QAction("delta", self)
        delta.setCheckable(True)
        toolbar.addAction(delta)
        self.delta_action = delta

        widget = QWidget(self)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def remove_central_layout_child(self, idx=0):
        if central_layout := self.centralWidget().layout():
            if target_item := central_layout.itemAt(idx):
                # safe-casting
                if target_widget := target_item.widget():
                    target_widget.deleteLater()

    @property
    def central_widget_layout(self) -> QVBoxLayout:
        return self.centralWidget().layout()


class MockCell(QWidget):
    def __init__(self, color: str, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = MockWindow()
    window.show()
    app.exec()

