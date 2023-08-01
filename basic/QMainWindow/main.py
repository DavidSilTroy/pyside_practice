from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# Creating application with QApplication
app = QApplication([])

# Creating main window
window = QMainWindow()
window.setWindowTitle("My app with PySide6")

# creating widget
label = QLabel("Hello World!")

# adding widget to Main Window
window.setCentralWidget(label)

# Show Window
window.show()

# Running the application
app.exec()