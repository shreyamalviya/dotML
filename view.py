from PyQt5.QtWidgets import QApplication, QLabel, QGroupBox, QFrame, QVBoxLayout, QDialog, QRadioButton, QGridLayout

class View(QDialog):
    def __init__(self):
        super(View, self).__init__(None)
        self.createOutputWidget()
        self.createDataWidget()
        self.createGraphWidget()
        self.createConsoleWidget()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.OutputWidget, 0, 0, 3, 3)
        mainLayout.addWidget(self.DataWidget, 0, 4, 3, 1)
        mainLayout.addWidget(self.GraphWidget, 4, 0, 2, 3)
        mainLayout.addWidget(self.ConsoleWidget, 4, 4, 2, 1)

        self.setLayout(mainLayout)

    def createOutputWidget(self):
        self.OutputWidget = QGroupBox("Output")

        temp = QRadioButton("1")
        layout = QVBoxLayout()
        layout.addWidget(temp)
        layout.addStretch()
        self.OutputWidget.setLayout(layout)

    def createDataWidget(self):
        self.DataWidget = QGroupBox("Dataset")

        temp = QRadioButton("2")
        layout = QVBoxLayout()
        layout.addWidget(temp)
        layout.addStretch()
        self.DataWidget.setLayout(layout)
    
    def createGraphWidget(self):
        self.GraphWidget = QGroupBox("Graph")

        temp = QRadioButton("3")
        layout = QVBoxLayout()
        layout.addWidget(temp)
        layout.addStretch()
        self.GraphWidget.setLayout(layout)
    
    def createConsoleWidget(self):
        self.ConsoleWidget = QGroupBox("Console")

        temp = QRadioButton("4")
        layout = QVBoxLayout()
        layout.addWidget(temp)
        layout.addStretch()
        self.ConsoleWidget.setLayout(layout)

def main():
    main_view = QApplication([])
    view = View()
    view.resize(700, 700)
    view.show()
    main_view.exec_()

if __name__ == "__main__":
    main()