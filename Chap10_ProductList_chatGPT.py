import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.setupDatabaseConnection()
        self.createProductsTable()

        self.populateTable()

    def setupUi(self):
        self.form_class = uic.loadUiType("Chap10_ProductList.ui")[0]
        self.ui = self.form_class()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.ui.tableWidget.setTabKeyNavigation(False)

        self.ui.prodID.returnPressed.connect(lambda: self.ui.prodName.setFocus())
        self.ui.prodName.returnPressed.connect(lambda: self.ui.prodPrice.setFocus())
        self.ui.prodPrice.returnPressed.connect(lambda: self.addProduct())

        self.ui.btnAdd.clicked.connect(self.addProduct)
        self.ui.btnUpdate.clicked.connect(self.updateProduct)
        self.ui.btnDelete.clicked.connect(self.removeProduct)
        self.ui.tableWidget.doubleClicked.connect(self.onTableDoubleClicked)

    def setupDatabaseConnection(self):
        self.conn = sqlite3.connect("ProductList.db")
        self.cur = self.conn.cursor()

    def createProductsTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER)")

    def populateTable(self):
        self.ui.tableWidget.clearContents()

        self.cur.execute("SELECT * FROM Products")
        for row, item in enumerate(self.cur.fetchall()):
            for col, value in enumerate(item):
                item_str = "{:10}".format(value) if col in (0, 2) else value
                table_item = QTableWidgetItem(str(item_str))
                if col in (0, 2):
                    table_item.setTextAlignment(Qt.AlignRight)
                self.ui.tableWidget.setItem(row, col, table_item)

    def addProduct(self):
        name = self.ui.prodName.text()
        price = int(self.ui.prodPrice.text())
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?)", (name, price))
        self.conn.commit()
        self.populateTable()

    def updateProduct(self):
        id = self.ui.prodID.text()
        name = self.ui.prodName.text()
        price = int(self.ui.prodPrice.text())
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?", (name, price, id))
        self.conn.commit()
        self.populateTable()

    def removeProduct(self):
        id = self.ui.prodID.text()
        self.cur.execute("DELETE FROM Products WHERE id=?", (id,))
        self.conn.commit()
        self.populateTable()

    def onTableDoubleClicked(self):
        current_row = self.ui.tableWidget.currentRow()
        id_item = self.ui.tableWidget.item(current_row, 0)
        name_item = self.ui.tableWidget.item(current_row, 1)
        price_item = self.ui.tableWidget.item(current_row, 2)

        self.ui.prodID.setText(id_item.text())
        self.ui.prodName.setText(name_item.text())
        self.ui.prodPrice.setText(price_item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    product_manager = DemoForm()
    product_manager.show()
    sys.exit(app.exec_())
