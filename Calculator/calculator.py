import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, 
                            QPushButton, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Calculator")
        self.setGeometry(100, 100, 350, 500)
        
        # Set dark theme
        self.set_dark_theme()
        
        # Main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Add some decorative elements
        self.add_decoration()
        
    def set_dark_theme(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)
        
    def create_display(self):
        # Display widget
        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        
        # Font settings
        display_font = QFont()
        display_font.setPointSize(24)
        self.result_display.setFont(display_font)
        
        # Style
        self.result_display.setStyleSheet(
            "background-color: #1E1E1E;"
            "color: #FFFFFF;"
            "border: 2px solid #555;"
            "border-radius: 5px;"
            "padding: 10px;"
        )
        
        self.layout.addWidget(self.result_display)
        
    def create_buttons(self):
        self.grid_layout = QGridLayout()
        
        # Button definitions with style
        buttons = [
            ('C', 0, 0, 1, 1, 'background-color: #FF5555;'),  # Red
            ('⌫', 0, 1, 1, 1, 'background-color: #5555FF;'),  # Blue (backspace)
            ('%', 0, 2, 1, 1, 'background-color: #333333;'),  # Dark gray
            ('/', 0, 3, 1, 1, 'background-color: #333333;'),  # Dark gray
            
            ('7', 1, 0, 1, 1, 'background-color: #444444;'),  # Gray
            ('8', 1, 1, 1, 1, 'background-color: #444444;'),  # Gray
            ('9', 1, 2, 1, 1, 'background-color: #444444;'),  # Gray
            ('*', 1, 3, 1, 1, 'background-color: #333333;'),  # Dark gray
            
            ('4', 2, 0, 1, 1, 'background-color: #444444;'),  # Gray
            ('5', 2, 1, 1, 1, 'background-color: #444444;'),  # Gray
            ('6', 2, 2, 1, 1, 'background-color: #444444;'),  # Gray
            ('-', 2, 3, 1, 1, 'background-color: #333333;'),  # Dark gray
            
            ('1', 3, 0, 1, 1, 'background-color: #444444;'),  # Gray
            ('2', 3, 1, 1, 1, 'background-color: #444444;'),  # Gray
            ('3', 3, 2, 1, 1, 'background-color: #444444;'),  # Gray
            ('+', 3, 3, 1, 1, 'background-color: #333333;'),  # Dark gray
            
            ('0', 4, 0, 1, 2, 'background-color: #444444;'),  # Gray (span 2 columns)
            ('.', 4, 2, 1, 1, 'background-color: #444444;'),  # Gray
            ('=', 4, 3, 1, 1, 'background-color: #55AA55;'),  # Green
        ]
        
        # Create buttons and add to grid
        button_font = QFont()
        button_font.setPointSize(16)
        
        for (text, row, col, row_span, col_span, style) in buttons:
            button = QPushButton(text)
            button.setFont(button_font)
            button.setStyleSheet(
                f"color: white;"
                f"{style}"
                "border: none;"
                "border-radius: 5px;"
                "padding: 15px;"
            )
            
            # Hover effects
            button.setStyleSheet(button.styleSheet() + "QPushButton:hover { background-color: #666666; }")
            
            button.clicked.connect(self.on_button_click)
            self.grid_layout.addWidget(button, row, col, row_span, col_span)
        
        self.layout.addLayout(self.grid_layout)
        
    def add_decoration(self):
        # Add a decorative label at the bottom
        footer = QLabel("PyQt5 Calculator")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet(
            "color: #AAAAAA;"
            "font-size: 12px;"
            "padding: 10px;"
        )
        self.layout.addWidget(footer)
        
    def on_button_click(self):
        sender = self.sender()
        current_text = self.result_display.text()
        
        if sender.text() == 'C':
            self.result_display.clear()
        elif sender.text() == '⌫':  # Backspace
            self.result_display.setText(current_text[:-1])
        elif sender.text() == '=':
            try:
                # Replace % with /100 for percentage calculations
                expression = current_text.replace('%', '/100')
                result = eval(expression)
                self.result_display.setText(str(result))
            except Exception:
                self.result_display.setText("Error")
        else:
            new_text = current_text + sender.text()
            self.result_display.setText(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
