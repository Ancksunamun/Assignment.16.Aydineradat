
from math import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *





class calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader= QUiLoader()
        self.ui=loader.load('form.ui',None)
        self.ui.show()

        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_diff.clicked.connect(self.diff)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_equal.clicked.connect(self.equal)

        self.ui.btn_clear.clicked.connect(self.clear)

        self.selcted_oprator=''
        self.result=0

        self.ui.btn_1.clicked.connect(self.function1)
        self.ui.btn_2.clicked.connect(self.function2)
        self.ui.btn_3.clicked.connect(self.fucntion3)
        self.ui.btn_4.clicked.connect(self.fucntion4)
        self.ui.btn_5.clicked.connect(self.function5)
        self.ui.btn_6.clicked.connect(self.function6)
        self.ui.btn_7.clicked.connect(self.fucntion7)
        self.ui.btn_8.clicked.connect(self.fucntion8)
        self.ui.btn_9.clicked.connect(self.fucntion9)
        self.ui.btn_0.clicked.connect(self.fucntion0)
        self.ui.btn_point.clicked.connect(self.dat)

        self.ui.btn_sin.clicked.connect(self.sin1)
        self.ui.btn_cos.clicked.connect(self.cos1)
        self.ui.btn_tan.clicked.connect(self.tan1)
        self.ui.btn_cot.clicked.connect(self.cot1)
        self.ui.btn_log.clicked.connect(self.log1)
        self.ui.btn_sqrt.clicked.connect(self.sqrt1)


    def clear(self):
        self.ui.textbox.setText("")
        self.result=0

    #float or intiger
    def iorf(self):
        a=float(self.result)
        b=int(self.result)
        if a == b:
            return b
        else:
            return a

    def function1(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '1')
    def function2(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '2')
    def fucntion3(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '3')
    def fucntion4(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '4')
    def function5(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '5')
    def function6(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '6')
    def fucntion7(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '7')
    def fucntion8(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '8')
    def fucntion9(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '9')
    def fucntion0(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '0')

    def dat(self):
        if '.' in self.ui.textbox.text():
            pass
        else:
            self.ui.textbox.setText(self.ui.textbox.text()+'.')



    def sum(self):
        self.num1=float(self.ui.textbox.text())
        self.result += self.num1
        self.ui.textbox.setText('')
        self.selcted_oprator = "+"

    def diff(self):
        self.num1=float(self.ui.textbox.text())
        self.result += self.num1
        self.ui.textbox.setText('')
        self.selcted_oprator = "-"

    def mul(self):
        self.num1=float(self.ui.textbox.text())
        self.result = self.num1
        self.ui.textbox.setText('')
        self.selcted_oprator = "*"

    def div(self):
        self.num1=float(self.ui.textbox.text())
        self.result = self.num1
        self.ui.textbox.setText('')
        self.selcted_oprator = "/"

    def sin1(self):
        try:
            self.result=float(self.ui.textbox.text())
            self.ui.textbox.setText(str(format(sin(radians(self.result)),".4f")))
        except:
            print('ERROR')
    def cos1(self):
        try:
            self.result=float(self.ui.textbox.text())
            self.ui.textbox.setText(str(format(cos(radians(self.result)),".4f")))
        except:
            print('ERROR')

    def tan1(self):
        try:
            self.result=float(self.ui.textbox.text())
            self.ui.textbox.setText(str(format(tan(radians(self.result)),".4f")))
        except:
            print('ERROR')
    def cot1(self):
        try:
            self.result=float((self.ui.textbox.text())**-1)
            self.ui.textbox.setText(str(format(tan(radians(self.result)),".4f")))
        except:
            print('ERROR')
    def log1(self):
        try:
            self.result=float(self.ui.textbox.text())
            self.ui.textbox.setText(str(format(log10((self.result)),".4f")))
        except:
            print('ERROR')
    def sqrt1(self):
        try:
            self.result=float(self.ui.textbox.text())
            self.ui.textbox.setText(str(format(sqrt((self.result)),".4f")))
        except:
            print('ERROR')



    def equal(self):
        self.num2=float(self.ui.textbox.text())
        if  self.selcted_oprator == "+":
            self.result += self.num2
            self.ui.textbox.setText(str(self.result))

        if self.selcted_oprator == "-":
            self.result -= self.num2
            self.ui.textbox.setText(str(self.result))

        if self.selcted_oprator == "*":
            self.result *= self.num2
            self.ui.textbox.setText(str(self.result))

        if self.selcted_oprator == "/":
            try:
                self.result /= self.num2
                self.ui.textbox.setText(str(self.result))
            except:
                print("ERROR")















app=QApplication([])

window = calculator()
app.exec()
