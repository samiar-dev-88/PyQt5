# PyQt5
# Import libraries
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QTextEdit,
    QListWidget,
    QMessageBox,
    QMenuBar,
    QMenu,
    QAction,
    QFileDialog,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox
)

from PyQt5.QtGui import QPixmap # For image



# Creat Window
app = QApplication(sys.argv) # Creat app
window = QWidget() # Window
window.setWindowTitle("PyQt5 Complete Demo") # Title
window.resize(500, 500) # Size



# Layout
main_layout = QVBoxLayout() # Creat layout
window.setLayout(main_layout) # Put layout on window



# QLabel
label = QLabel("Hello, Welcome!") # Label
main_layout.addWidget(label) # Location



# QPushButton
button = QPushButton("Click me") # Button

def button_clicked():
    print("Clicked")

button.clicked.connect(button_clicked) # Button def
main_layout.addWidget(button) # Location



# QLineEdit
line_edit = QLineEdit() # Input
line_edit.setPlaceholderText("Enter anything...") # Text on it
main_layout.addWidget(line_edit) # Location
line_edit_value = line_edit.text() # Save value (str)
print(line_edit_value) # Print value
"""line_edit.clear()""" # Clear
"""line_edit.setEchoMode(QLineEdit.Password)""" # For write password



# QCheckBox
check_box = QCheckBox("I love python") # Check box
main_layout.addWidget(check_box) # Location
check_box_value = check_box.isChecked() # Save value (bool)



# QRadioButton
radio_python = QRadioButton("Python") # Radio button
radio_java = QRadioButton("Java") # Radio button
radio_python.setChecked(True) # Default choice
main_layout.addWidget(radio_python) # Location
main_layout.addWidget(radio_java) # Location
radio_java_value = radio_java.isChecked() # Save value (bool)
print(radio_java_value) # Print value



# QComboBox
combo_box = QComboBox() # Combo box
combo_box.addItem("Python") # Add item
combo_box.addItem("JavaScript") # Add item
combo_box.addItem("C++") # Add item
combo_box.addItem("Java") # Add item
main_layout.addWidget(combo_box) # Location
combo_box_value = combo_box.currentText() # Save value (str)
print(combo_box_value) # Print value



# QTextEdit
text_edit = QTextEdit() # Long input
main_layout.addWidget(text_edit) # Location
text_edit_value = text_edit.toPlainText() # Save value (str)
print(text_edit_value) # Print value
"""text_edit.clear()""" # Clear



# QListWidget
list_widget = QListWidget() # List
list_widget.addItem("Python") # Add item
list_widget.addItem("PyQt5") # Add item
list_widget.addItem("HTML") # Add item
list_widget.addItem("CSS") # Add item
list_widget.addItem("JavaScript") # Add item
main_layout.addWidget(list_widget) # Location
list_widget_value = list_widget.currentItem() # Save value (str)
print(list_widget_value) # Print value



# QPixmap
image_label = QLabel() # Creat a label
pixmap = QPixmap(r"D:\CLASS\Python - 201\PyQt5\1.png") # Image
image_label.setPixmap(pixmap) # Location(label)
scaled_pixmap = pixmap.scaled(200 , 150 , aspectRatioMode=1) # Image size
image_label.setPixmap(scaled_pixmap) # Location(sized image)
main_layout.addWidget(image_label) # Location(image)



# QDialog
def open_dialog():
    dialog = QDialog(window) # File dialog
    dialog.setWindowTitle("Dialog") # Title
    dialog.resize(400, 250) # Size
    dialog_layout = QVBoxLayout() # Layout
    dialog.setLayout(dialog_layout) # Layout

    dialog_label = QLabel("This is a QDialog")
    dialog_layout.addWidget(dialog_label)

    close_button = QPushButton("Exit")
    close_button.clicked.connect(dialog.close)
    dialog_layout.addWidget(close_button)

    dialog.exec_() # Show App (The first window is not working)
    """dialog.show()""" # Show App 

dialog_button = QPushButton("Open QDialog")
dialog_button.clicked.connect(open_dialog)
main_layout.addWidget(dialog_button)



# QMessageBox
"""
    # information
QMessageBox.information(
    window,
    "Information",
    "این یک پیام اطلاعاتی است"
)
    # question
answer = QMessageBox.question(
    window,
    "Question",
    "Do you love python?",
    QMessageBox.Yes | QMessageBox.No
)
    # For question
if answer == QMessageBox.Yes:
    print("Yes")
else:
    print("No")

    # Another modes: critical , warning
"""



# QFileDialog
def open_file():
    
    file_path, _ = QFileDialog.getOpenFileName(
        window,
        "Open", # Title
        "", # Default text
        "Text Files (*.txt);;All Files (*)" # Just txt
    )
    if file_path: # If chossed
        print("Chossed:")
        print(file_path)

def save_file():
    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "Save", # Title
        "", # Default text
        "Text Files (*.txt);;All Files (*)" # Save as txt
    )
    if file_path: # If chossed
        print("Saves:")
        print(file_path)



# QMenuBar
menu_bar = QMenuBar() # Menubar


file_menu = menu_bar.addMenu("File") # Option1

open_action = QAction("Open", window) # Action1
open_action.triggered.connect(open_file) # Action1 def
file_menu.addAction(open_action) # For action1

save_action = QAction("Save", window) # Action2
save_action.triggered.connect(save_file) # Action2 def
file_menu.addAction(save_action) # For action2

file_menu.addSeparator() # Line
 
exit_action = QAction("Exit", window) # Action3
# Close App
exit_action.triggered.connect(app.quit) # Action3 def
file_menu.addAction(exit_action) # For action3

exit_action.setShortcut("Ctrl+C") # Shortcut


edit_menu = menu_bar.addMenu("Edit") # Option2

copy_action = QAction("Copy", window) # Action1
edit_menu.addAction(copy_action) # Action1

paste_action = QAction("Paste", window) # Action2
edit_menu.addAction(paste_action) # For action2

main_layout.insertWidget(0, menu_bar) # Put the menu top of the page
"""main_layout.addWidget(menu_bar)""" # If it was top of the all widgets

# QSS
"""label.setText("...")""" # Change Text

window.setStyleSheet(""" # Style
    QLabel {
        color: #ffffff;
        font-size: 20px;
        font-weight: bold;
    } 

    QMainWindow {
        background-color: #202124;
    }

    QLabel {
        color: white;
    }

    QPushButton {
        background-color: #303134;
        color: white;
        padding: 8px;
        border-radius: 6px;
    }

    QPushButton:hover {
        background-color: #45474a;
    }

    QPushButton:pressed {
        background-color: #111111;
    }

    QPushButton:focus {
        border: 1px solid #ffffff;
    }

    QLineEdit {
        background-color: #303134;
        color: white;
        padding: 8px;
        border: 1px solid #555555;
        border-radius: 5px;
    }

    QTextEdit {
        background-color: #303134;
        color: white;
    }

    QComboBox {
        background-color: #303134;
        color: white;
        padding: 7px;
    }

    QListWidget {
        background-color: #303134;
        color: white;
    }

    QCheckBox {
        color: white;
    }

    QRadioButton {
        color: white;
    }

    QMenuBar {
        background-color: #202124;
        color: white;
    }

    QMenuBar::item:selected {
        background-color: #45474a;
    }

    QMenu {
        background-color: #303134;
        color: white;
    }

    QMenu::item:selected {
        background-color: #45474a;
    }
""")




window.show() # Show Window
sys.exit(app.exec_()) # Run App