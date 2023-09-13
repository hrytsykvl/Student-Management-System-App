import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time(hours): ")
        self.time_line_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Imperial(miles)', 'Metric(km)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.result_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        speed = distance / time

        # Check what user chose in combo
        if self.unit_combo.currentText() == 'Imperial(miles)':
            speed = round(speed * 0.621371, 2)
            unit = "mph"
        if self.unit_combo.currentText() == 'Metric(km)':
            speed = round(speed, 2)
            unit = "km/h"

        self.result_label.setText(f"Average speed is {speed} {unit}")


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
sys.exit(app.exec())
