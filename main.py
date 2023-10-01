import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from functools import partial
from evaluate import Calculate

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.Central=QWidget(self)
        self.setCentralWidget(self.Central)
        self.setFixedSize(250,400)
        self.line={}
        self.flag=0
        self.dr=1
        self.layout1()
        self.layout2()
        self.mainlayout()
        self.ui()
        self.signal()
    def layout1(self):       
        self.page1=QWidget()
        self.l1=QGridLayout()
        self.l1.setSpacing(4)
        self.buttons={}
        b={'1':(3,0),
           '2':(3,1),
           '3':(3,2),
           '4':(2,0),
           '5':(2,1),
           '6':(2,2),
           '7':(1,0),
           '8':(1,1),
           '9':(1,2),
           '0':(4,0),
           '⌫':(0,3),
           '.':(4,1),
           '+':(3,3),
           '-':(4,2),
           '*':(2,3),
           '/':(1,3),
           '(':(0,1),
           ')':(0,2),
           '=':(4,3),
           'C':(0,0)}
        for name,pos in b.items():
            self.buttons[name]=QPushButton(name)
            self.buttons[name].setFixedSize(50,50)
            self.l1.addWidget(self.buttons[name],pos[0],pos[1])     
        self.line[1]=QLineEdit()
        self.line[1].setFixedHeight(60)
        self.line[1].setAlignment(Qt.AlignRight)
        self.line[1].setPlaceholderText('0')
        self.v1=QVBoxLayout(self.page1)
        self.v1.addWidget(self.line[1])
        self.v1.addLayout(self.l1)
        self.page1.setLayout(self.v1)
    def layout2(self):
        self.page2=QWidget()
        self.l2=QGridLayout()
        self.l2.setSpacing(4)
        self.buttons2={}
        b2={'1':(3,3),
            '2':(3,4),
            '3':(3,5),
            '4':(2,3),
            '5':(2,4),
            '6':(2,5),
            '7':(1,3),
            '8':(1,4),
            '9':(1,5),
            '0':(4,3),
            '.':(4,4),
            '+':(3,6),
            '-':(4,5),
            '*':(2,6),
            '/':(1,6),
            '(':(0,4),
            ')':(0,5),
            '=':(4,6),
            'C':(0,3),
            'pi':(0,2),
            'e':(0,1),
            'sin':(1,1),
            'cos':(2,1),
            'tan':(3,1),
            'log':(4,0),
            '√':(1,2),
            '^':(2,2),
            '⌫':(0,6),
            'asin':(1,0),
            'acos':(2,0),
            'atan':(3,0),
            'ln':(4,1),
            '!':(3,2),
            'mod':(4,2)}
        self.deg_rad=QPushButton('deg')
        self.deg_rad.setFixedSize(50,50)
        self.l2.addWidget(self.deg_rad,0,0)
        for name,pos in b2.items():
            self.buttons2[name]=QPushButton(name)
            self.buttons2[name].setFixedSize(50,50)
            self.l2.addWidget(self.buttons2[name],pos[0],pos[1])
        self.line[2]=QLineEdit()
        self.line[2].setFixedHeight(60)
        self.line[2].setAlignment(Qt.AlignRight)
        self.line[2].setPlaceholderText('0')
        self.v2=QVBoxLayout(self.page2)
        self.v2.addWidget(self.line[2])
        self.v2.addLayout(self.l2)
        self.page2.setLayout(self.v2)
    def mainlayout(self):        
        self.layout=QVBoxLayout()
        self.stack=QStackedLayout()
        self.hal=QHBoxLayout()
        self.group=QButtonGroup()
        self.b1=QRadioButton()
        self.b2=QRadioButton()
        self.group.addButton(self.b1)
        self.group.addButton(self.b2)
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2) 
        self.hal.addWidget(self.b1)
        self.hal.addWidget(self.b2)
        self.layout.addLayout(self.hal)
        self.layout.addLayout(self.stack)
        self.Central.setLayout(self.layout)
    def ui(self):
        self.Central.setStyleSheet("background-color : #010101")
        for name in self.buttons.keys():
            if name not in "()/*+-=C⌫": 
                self.buttons[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : white;font-size : 16px")
            elif name in "()/*+-⌫":
                self.buttons[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : #9cd260;font-size : 16px")
            elif name == '=':
                self.buttons[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #427e04;color : white;font-size : 16px;font-weight : bold")
            elif name in "C":
                self.buttons[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : #e3694c;font-size : 16px")
        self.line[1].setStyleSheet("color : white;font-size : 24px; qproperty-frame : false")
        for name in self.buttons2.keys():
            if name not in "()/*+-=C⌫": 
                self.buttons2[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : white;font-size : 16px")
            elif name in "()/*+-⌫":
                self.buttons2[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : #9cd260;font-size : 16px")
            elif name == '=':
                self.buttons2[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #427e04;color : white;font-size : 16px;font-weight : bold")
            elif name in "C":
                self.buttons2[name].setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : #e3694c;font-size : 16px")
        self.deg_rad.setStyleSheet("border-radius : 25;border-style : outset;border-width : 1px;border-color : #333333;background-color : #171717;color : #9cd260;font-size : 16px")
        self.line[2].setStyleSheet("color : white;font-size : 24px; qproperty-frame : false")
        self.b1.setStyleSheet("QRadioButton::indicator::unchecked {image: url(calc_disabled.png);}QRadioButton::indicator::checked {image: url(calc_enabled.png);}QRadioButton::indicator{width : 30;height : 30;}")
        self.b2.setStyleSheet("QRadioButton::indicator::unchecked {image: url(sci_disabled.png);}QRadioButton::indicator::checked {image: url(sci_enabled.png);}QRadioButton::indicator{width : 30;height : 30;}")
    def signal(self):
        self.b1.toggled.connect(self.calc)
        self.b1.setChecked(True)
        self.b2.toggled.connect(self.scicalc)
        self.line[1].textEdited.connect(self.removeChar)
        self.line[2].textEdited.connect(self.removeChar)
        self.buttons['⌫'].clicked.connect(self.backspace)        
        self.buttons2['⌫'].clicked.connect(self.backspace)
        for name,button in self.buttons.items():
            if name not in '=C⌫':
                button.clicked.connect(partial(self.write,name))
        for name,button in self.buttons2.items():
            if name not in '=C⌫':
                button.clicked.connect(partial(self.write,name))
        self.buttons['C'].clicked.connect(self.erase)
        self.buttons['='].clicked.connect(self.evaluate)
        self.buttons2['C'].clicked.connect(self.erase)
        self.buttons2['='].clicked.connect(self.evaluate)
        self.line[1].returnPressed.connect(self.evaluate)
        self.line[2].returnPressed.connect(self.evaluate)
        self.deg_rad.clicked.connect(self.switch)
    def switch(self):
        if self.dr==1:
            self.dr=2
            self.deg_rad.setText('rad')
        elif self.dr==2:
            self.dr=1
            self.deg_rad.setText('deg')
    def backspace(self):
        st=self.line[self.flag].displayText()
        try:
            self.line[self.flag].backspace()
        except:
            self.line[self.flag].clear()
    def removeChar(self):
        st=self.line[self.flag].displayText()
        try:
            if self.flag==1:
                if st[-1] not in '1234567890()-+/*.':
                    self.line[self.flag].backspace()
            elif self.flag==2:
                if st[-1] not in '1234567890()-+/*.√^!epicosintanlgmd':
                    self.line[self.flag].backspace()
        except:
            self.line[self.flag].clear()
    def erase(self):
        self.line[self.flag].clear()
    def evaluate(self):
        s=self.line[self.flag].displayText()
        while s.count('(')>s.count(')'):
            temp=s+')'
            s=temp
        if self.flag==1:
            try:
                ans=str(eval(s))
            except:
                ans='ERROR'
        elif self.flag==2:
            c=Calculate()
            try:
                ans=c.bracket(s,self.dr)
            except:
                ans='ERROR'
        self.line[self.flag].setText(ans)
    def write(self,name):
        exp=self.line[self.flag].displayText()
        exp=exp+name
        self.line[self.flag].setText(exp)
    def calc(self):
        self.flag=1
        self.setFixedSize(250,400)
        self.stack.setCurrentIndex(0)
    def scicalc(self):
        self.flag=2
        self.setFixedSize(410,400)
        self.stack.setCurrentIndex(1)       
def main():
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
main()
