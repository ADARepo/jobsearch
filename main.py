from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
import requests
import sys

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", 
        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
        "West Virginia", "Wisconsin", "Wyoming"]

# The main search window.
class Window(QMainWindow):
    

    def __init__(self):
        super().__init__()        
        
        # Fixed sizes of window
        width = 700
        height = 300
        
        # Window attributes.
        self.setWindowTitle("Job Search")
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        # Job keyword label positioning.
        self.label1 = QLabel("Job Keyword(s)", self)
        self.label1.move(int(width / 2 - 250), int(height / 2 - 100))
        self.label1.setFont(QFont('Times', 12, QFont.Bold))
        self.label1.resize(130, 80)

        # Job title text box.
        self.jobBox = QLineEdit(self)
        self.jobBox.move(int(width / 2 - 280), int(height / 2 - 50))
        self.jobBox.setFont(QFont('Times', 12))
        self.jobBox.resize(200, 30)

        # City/State location.
        self.label2 = QLabel("City/State", self)
        self.label2.move(int(width / 2 + 68), int(height / 2 - 100))
        self.label2.setFont(QFont('Times', 12, QFont.Bold))
        self.label2.resize(100, 80)

        # City text box.
        self.cityBox = QLineEdit(self)
        self.cityBox.move(int(width / 2), int(height / 2 - 50))
        self.cityBox.setFont(QFont('Times', 12))
        self.cityBox.resize(200, 30)

        # State text box.
        self.combo = QComboBox(self)
        self.combo.addItems(states)
        self.combo.move(int(width / 2), int(height / 2 - 20))
        self.combo.setFont(QFont('Times', 12))
        self.combo.resize(200, 30)

        # Submit button. Will handle parsing job sites at this point.
        self.submitButton = QPushButton(self)
        self.submitButton.move(int(width / 2 - 120), int(height / 2 + 50))
        self.submitButton.setText("Submit")
        self.submitButton.resize(100, 30)
        self.submitButton.setFont(QFont('Times', 10, QFont.Bold))
        self.submitButton.clicked.connect(self.on_click)

        # Show the Frame/Window.
        self.show()

    # Submit button was clicked, check to see if fields have valid entries. Checking empty string for now.
    @pyqtSlot()
    def on_click(self):
        jobEntry = self.jobBox.text()
        cityEntry = self.cityBox.text()

        # Check for entry into job keyword and city entry.
        if jobEntry == "" or cityEntry == "":
            msg = QMessageBox()
            msg.setWindowTitle("Missing entries.")
            msg.setText("Please enter a city and job keyword.")
            msg.exec_()
        else:
            stateEntry = self.combo.currentText()
            jobTerms = jobEntry.split()

            print(len(jobTerms))
            print(jobTerms[1])

            # Base url for indeed. Need to parse out the job entry before appending to url string.
            indeedUrl = "https://www.indeed.com/jobs?q=" + jobTerms[0]

            for i in range(1, len(jobTerms)):
                indeedUrl += '+' + jobTerms[i]
            
            # Appending final params for city and state before making a GET request.
            indeedUrl += "&l=" + cityEntry + "+" + stateEntry

            html = requests.get(indeedUrl)

            print(html.text)

            # With the state, city, and job, we can now use BeautifulSoup to grab the data from job sites.




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())