import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stoppuhr')
        self.resize(250, 130)
        self.layout = QVBoxLayout()

        self.label = QLabel('00:00:000', self)
        self.label.setStyleSheet('font-size: 32px; qproperty-alignment: AlignCenter;')
        self.layout.addWidget(self.label)

        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stopp')
        self.reset_button = QPushButton('Reset')
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.reset_button)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.elapsed = 0
        self.running = False

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def update_time(self):
        self.elapsed += 10
        minutes = self.elapsed // 60000
        seconds = (self.elapsed // 1000) % 60
        msecs = self.elapsed % 1000
        self.label.setText(f"{minutes:02d}:{seconds:02d}:{msecs:03d}")

    def start(self):
        if not self.running:
            self.timer.start(10)
            self.running = True

    def stop(self):
        if self.running:
            self.timer.stop()
            self.running = False

    def reset(self):
        self.timer.stop()
        self.elapsed = 0
        self.label.setText('00:00:000')
        self.running = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Stopwatch()
    win.show()
    sys.exit(app.exec_())
