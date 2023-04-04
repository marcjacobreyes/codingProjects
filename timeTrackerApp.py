import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit

class TimeSheetCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set the window properties
        self.setWindowTitle("Time Sheet Calculator")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: green; color: yellow;")

        # Set the window layout
        grid = QGridLayout()
        grid.setSpacing(10)

        # Add days and times layouts
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        times = ["Time In", "Time Out"]

        for i, day in enumerate(days):
            # Add the day label to the layout
            day_label = QLabel(day)
            grid.addWidget(day_label, i+1, 0)

            for j, time in enumerate(times):
                # Add the time label to the layout
                time_label = QLabel(time)
                grid.addWidget(time_label, 0, j+1)

                # Add the time entry to the layout
                time_entry = QLineEdit()
                time_entry.textChanged.connect(lambda text, day=day: self.calculate_total_hours(day))
                grid.addWidget(time_entry, i+1, j+1)

        # Add the total hours label to the layout
        total_hours_label = QLabel("Total Hours")
        grid.addWidget(total_hours_label, len(days)+1, 0)

        self.total_hours_entry = QLineEdit()
        self.total_hours_entry.setReadOnly(True)
        grid.addWidget(self.total_hours_entry, len(days)+1, 1)

        # Set the layout for the window
        self.setLayout(grid)

    def calculate_total_hours(self, day):
        # Get the time in and out for the day
        time_in_entry = self.findChild(QLineEdit, day + " Time In")
        time_out_entry = self.findChild(QLineEdit, day + " Time Out")

        time_in = time_in_entry.text()
        time_out = time_out_entry.text()

        if time_in and time_out:
            # Calculate the total hours worked
            time_in_hours, time_in_minutes = map(int, time_in.split(":"))
            time_out_hours, time_out_minutes = map(int, time_out.split(":"))

            total_minutes = (time_out_hours - time_in_hours) * 60 + time_out_minutes - time_in_minutes
            total_hours = total_minutes / 60

            # Update the total hours entry
            self.total_hours_entry.setText("{:.2f}".format(total_hours))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    time_sheet_calculator = TimeSheetCalculator()
    time_sheet_calculator.show()
    sys.exit(app.exec_())
