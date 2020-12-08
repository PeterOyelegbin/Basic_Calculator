# PetitCalc
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon, QFont, QPixmap, QColor

class Calculator:
    def __init__(self):
        # Create label widget
        lbl = QLabel('BasicCalc')
        lbl.setFont(QFont('Forte', 30))
        lbl.setStyleSheet('color:magenta;')
        vb.addWidget(lbl)

        # Create input frame
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont('Arial Bold', 20))
        self.input_field.setStyleSheet('color:blue;')
        self.input_field.setReadOnly(True)
        vb.addWidget(self.input_field)

        # Create button frame
        btns_frame = QFrame()
        vb.addWidget(btns_frame)

        # Add buttons to frame
        grid = QGridLayout(btns_frame)
        self.clear = QPushButton('C', clicked=lambda: self.btn_clear())
        self.clear.setPalette(red)
        grid.addWidget(self.clear, 0,0)
        self.openbracket = QPushButton('(', clicked=lambda: self.btn_click('('))
        self.openbracket.setPalette(gray)
        grid.addWidget(self.openbracket, 0,1)
        self.closebracket = QPushButton(')', clicked=lambda: self.btn_click(')'))
        self.closebracket.setPalette(gray)
        grid.addWidget(self.closebracket, 0,2)
        self.divide = QPushButton('/', clicked=lambda: self.btn_click('/'))
        self.divide.setPalette(gray)
        grid.addWidget(self.divide, 0,3)

        self.seven = QPushButton('7', clicked=lambda: self.btn_click(7))
        grid.addWidget(self.seven, 1,0)
        self.eight = QPushButton('8', clicked=lambda: self.btn_click(8))
        grid.addWidget(self.eight, 1,1)
        self.nine = QPushButton('9', clicked=lambda: self.btn_click(9))
        grid.addWidget(self.nine, 1,2)
        self.multiply = QPushButton('x', clicked=lambda: self.btn_click('*'))
        self.multiply.setPalette(gray)
        grid.addWidget(self.multiply, 1,3)

        self.four = QPushButton('4', clicked=lambda: self.btn_click(4))
        grid.addWidget(self.four, 2,0)
        self.five = QPushButton('5', clicked=lambda: self.btn_click(5))
        grid.addWidget(self.five, 2,1)
        self.six = QPushButton('6', clicked=lambda: self.btn_click(6))
        grid.addWidget(self.six, 2,2)
        self.minus = QPushButton('-', clicked=lambda: self.btn_click('-'))
        self.minus.setPalette(gray)
        grid.addWidget(self.minus, 2,3)

        self.one = QPushButton('1', clicked=lambda: self.btn_click(1))
        grid.addWidget(self.one, 3,0)
        self.two = QPushButton('2', clicked=lambda: self.btn_click(2))
        grid.addWidget(self.two, 3,1)
        self.three = QPushButton('3', clicked=lambda: self.btn_click(3))
        grid.addWidget(self.three, 3,2)
        self.plus = QPushButton('+', clicked=lambda: self.btn_click('+'))
        self.plus.setPalette(gray)
        grid.addWidget(self.plus, 3,3)

        self.zero = QPushButton('0', clicked=lambda: self.btn_click(0))
        grid.addWidget(self.zero, 4,0)
        self.point = QPushButton('.', clicked=lambda: self.btn_click('.'))
        self.point.setPalette(gray)
        grid.addWidget(self.point, 4,1)
        self.power = QPushButton('^', clicked=lambda: self.btn_click('**'))
        self.power.setPalette(gray)
        grid.addWidget(self.power, 4,2)
        self.equals = QPushButton('=', clicked=lambda: self.btn_equal())
        self.equals.setPalette(blue)
        grid.addWidget(self.equals, 4,3)

    def btn_click(self, item):
        global expression
        expression = expression + str(item)
        self.input_field.setText(str(expression))

    def btn_clear(self):
        global expression
        expression = ""
        self.input_field.clear()

    def btn_equal(self):
        global expression
        result = str(eval(expression))
        self.input_field.setText(result)


app = QApplication([])
app.setStyle('Fusion')

# Set window and widget color
qp = QPalette()
qp.setColor(QPalette.Window, Qt.yellow)
qp.setColor(QPalette.Button, Qt.white)
app.setPalette(qp)

red = (QPalette(QColor(Qt.red)))
gray = (QPalette(QColor(Qt.gray)))
blue = (QPalette(QColor(Qt.blue)))

# Create window
win = QWidget()
win.setFixedSize(270,350)
win.setWindowTitle('BasicCalc')
win.setWindowIcon(QIcon('C:/Users/Hp/Desktop/Basic Calculator/images/Arithmetic.png'))
win.setFont(QFont('Arial Bold', 20))
    
# Create menu bar
vb = QVBoxLayout(win)
bar = QMenuBar()
bar.setNativeMenuBar(False)
Menu = bar.addMenu("≡ Menu")
vb.addWidget(bar)

# Add menu item
def about():
    dialog = QDialog()
    dialog.setWindowTitle('About')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(250,300)
    vb = QVBoxLayout(dialog)
    fme = QFrame()
    vb.addWidget(fme)
    grid = QGridLayout(fme)
    image = QPixmap("C:/Users/Hp/Desktop/Basic Calculator/images/Arithmetic.png")
    iproduct = QLabel()
    iproduct.setPixmap(image)
    iproduct.setScaledContents(True)
    iproduct.setFixedSize(70,50)
    grid.addWidget(iproduct, 0,0)
    
    product = QLabel('BasicCalc')
    product.setFont(QFont('Forte', 18))
    product.setStyleSheet('color:magenta;')
    grid.addWidget(product, 0,1)

    frame = QGroupBox('Developed by:')
    vb.addWidget(frame)
    form = QFormLayout(frame)
    details = QLabel('Name: Peter Oyelegbin \n\nWhatsApp: 08078828296 \n\nGmail: peteroyelegbin@gmail.com \n\n© 2020')
    form.addRow(details)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()
    
About = QAction("About", triggered=about)
Menu.addAction(About)

Quit = QAction("Quit", triggered=win.close)
Quit.setShortcut('Ctrl+Q')
Quit.setStatusTip('Exit application')
Menu.addAction(Quit)

# Assign operation variables
expression = ""

PetitCalc = Calculator()

win.show()
app.exec_()
