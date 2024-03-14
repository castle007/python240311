import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 


if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")


form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.id = 0 
        self.name = ""
        self.price = 0 

        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        self.getProduct()

    def addProduct(self):
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("insert into Products (Name, Price) values(?,?);", 
            (self.name, self.price))
        self.getProduct() 
        con.commit() 

    def updateProduct(self):
        self.id  = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("update Products set name=?, price=? where id=?;", 
            (self.name, self.price, self.id))
        self.getProduct() 
        con.commit()  

    def removeProduct(self):
        self.id  = self.prodID.text() 
        strSQL = "delete from Products where id=" + str(self.id)
        cur.execute(strSQL)
        self.getProduct() 
        con.commit()  

    def getProduct(self):
        self.tableWidget.clearContents()

        cur.execute("select * from Products;") 
        row = 0 
        for item in cur: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1
            print("row: ", row)  

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
