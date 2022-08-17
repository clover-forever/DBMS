from asyncio.windows_events import NULL
import sys
import random
import mysql.connector
from numpy import common_type, place
from gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QPushButton
from mysql.connector import Error

try:

    mydb = mysql.connector.connect(user='root',
                                host='127.0.0.1',
                                password='yourpwd',
                                database='singer_database')
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)


mycursor = mydb.cursor()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()
        self.text_browser_init()

    def text_browser_init(self):
        self.textBrowser.clear()

    def set_table_widget(self, data, attr_names): 
        self.tableWidget.setRowCount(len(data))
        if (len(data) == 0):
            pass
        else:
            self.tableWidget.setColumnCount(len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[row])):
                newitem = QTableWidgetItem(str(data[row][col]))
                self.tableWidget.setItem(row, col, newitem)

        self.tableWidget.setHorizontalHeaderLabels(attr_names)

    def onBindingUI(self):    
        self.pushButton.clicked.connect(self.on_pushButton_click)       # create singer
        self.pushButton_2.clicked.connect(self.on_pushButton_2_click)   # create album
        self.pushButton_3.clicked.connect(self.on_pushButton_3_click)   # create concert
        self.pushButton_4.clicked.connect(self.on_pushButton_4_click)   # create ceremony
        self.pushButton_5.clicked.connect(self.on_pushButton_5_click)   # create company
        self.pushButton_6.clicked.connect(self.on_pushButton_6_click)   # 10 querys
        self.pushButton_7.clicked.connect(self.on_pushButton_7_click)   # update singer's company
        self.pushButton_8.clicked.connect(self.on_pushButton_8_click)   # SQL輸入法
        self.pushButton_9.clicked.connect(self.on_pushButton_9_click)   # update album's ce_id
        self.pushButton_10.clicked.connect(self.on_pushButton_10_click)   # 查詢主持人為Anne的屆數 s-f-w 
        self.pushButton_11.clicked.connect(self.on_pushButton_11_click)   # 驚曲獎因疫情取消 delete 

    def on_pushButton_click(self): #create singer
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = "INSERT INTO Singer (SSN, s_name, birthday, zodiac_sign, sex, com_id) VALUES (%s, %s, %s, %s, %s, %s)"
        SSN = self.lineEdit.text()
        s_name = self.lineEdit_2.text()
        birthday = self.lineEdit_3.text()
        zodiac_sign = self.lineEdit_4.text()
        sex = self.lineEdit_5.text()
        com_id = self.lineEdit_6.text()
        
        if com_id.lower() == "null":
            com_id = None

        val = (SSN, s_name, birthday, zodiac_sign, sex, com_id)
        
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(
                sql % (SSN, s_name, birthday, zodiac_sign, sex, com_id))
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_2_click(self): # create Album
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = "INSERT INTO Album (a_id, a_date, title, SSN, ce_id) VALUES (%s, %s, %s, %s, %s)"
        a_id = self.lineEdit_9.text()
        a_date = self.lineEdit_10.text()
        title = self.lineEdit_11.text()
        SSN = self.lineEdit_12.text()
        ce_id = self.lineEdit_13.text()
        
        if SSN.lower() == "null":
            SSN = None
        if ce_id.lower() == "null":
            ce_id = None

        val = (a_id, a_date, title, SSN, ce_id)
        try:
            mycursor.execute(sql, val)
            mydb.commit()

            self.textBrowser.append(
                sql % (a_id, a_date, title, SSN, ce_id))

        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")
    
    def on_pushButton_3_click(self): # create Concert
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = "INSERT INTO Concert (con_id, place, con_year, con_name, SSN) VALUES (%s, %s, %s, %s, %s)"
        con_id = self.lineEdit_16.text()
        place = self.lineEdit_17.text()
        con_year = self.lineEdit_18.text()
        con_name = self.lineEdit_19.text()
        SSN = self.lineEdit_20.text()
        
        if SSN.lower() == "null":
            SSN = None

        val = (con_id, place, con_year, con_name, SSN)
        try:
            mycursor.execute(sql, val)
            mydb.commit()

            self.textBrowser.append(
                sql % (con_id, place, con_year, con_name, SSN))

        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_4_click(self): # create ceremony
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = "INSERT INTO Ceremony (ce_id, host_name, ce_place) VALUES (%s, %s, %s)"
        ce_id = self.lineEdit_21.text()
        host_name = self.lineEdit_22.text()
        ce_place = self.lineEdit_23.text()

        val = (ce_id, host_name, ce_place)
        try:
            mycursor.execute(sql, val)
            mydb.commit()

            self.textBrowser.append(
                sql % (ce_id, host_name, ce_place))

        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_5_click(self): #create company
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = "INSERT INTO Company (com_id, com_name, revenue, SSN) VALUES (%s, %s, %s, %s)"
        com_id = self.lineEdit_25.text()
        com_name = self.lineEdit_26.text()
        revenue = int(self.lineEdit_27.text())
        SSN = self.lineEdit_28.text()
        
        if SSN.lower() == "null":
            SSN = None

        val = (com_id, com_name, revenue, SSN)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(
                self.textBrowser.append(
                sql % (com_id, com_name, revenue, SSN)))

        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_6_click(self): # 10 queries
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        option = self.comboBox_4.currentIndex()
        if option == 0: #在高雄舉辦的演唱會名稱(IN)
            sql = f"SELECT `con_name` FROM `Concert` WHERE `place` IN ('高雄')"
            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(self.textBrowser.append(sql))
            
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")
        elif option == 1: #不在高雄舉辦的演唱會名稱(NOT IN)
            sql = f"SELECT `con_name` FROM `Concert` WHERE `place` NOT IN ('高雄')"
            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(self.textBrowser.append(sql))
            
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")
        elif option == 2: #在1999年發行專輯的歌手名字 (EXISTS)
            sql = f"SELECT `s_name` FROM `Singer` WHERE EXISTS (SELECT * FROM `Album` WHERE Singer.SSN = Album.SSN AND `a_date` = '1999')"
            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(self.textBrowser.append(sql))
            
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")
        elif option == 3: #不在1999年發行專輯的歌手名字 (NOT EXISTS)
            sql = f"SELECT `s_name` FROM `Singer` WHERE NOT EXISTS (SELECT * FROM `Album` WHERE Singer.SSN = Album.SSN AND `a_date` = '1999')"
            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(self.textBrowser.append(sql))
            
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 4: #總共有幾位歌手是雙子座 (COUNT)
            sql = f"SELECT COUNT(*) FROM `Singer` WHERE `zodiac_sign` = '雙子座'"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 5: #全部公司的年收入總合 (SUM)
            sql = f"SELECT SUM(`revenue`) FROM `Company`"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 6: #年收入最高的金額 (MAX)
            sql = f"SELECT MAX(`revenue`) FROM `Company`"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 7: #年收入最低的金額 (MIN)
            sql = f"SELECT MIN(`revenue`) FROM `Company`"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 8: #全部公司的平均收入 (AVG)
            sql = f"SELECT AVG(`revenue`) FROM `Company`"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

        elif option == 9: #找出年收入大於1000元的公司名稱 (HAV)
            sql = f"SELECT `com_name`, `revenue` FROM `Company` GROUP BY `com_name` HAVING Company.revenue > 1000"

            try:
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]
                self.set_table_widget(myresult, column_names)
                self.textBrowser.append(sql)

            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")
            

    def on_pushButton_7_click(self): # update singer's company
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        SSN = self.lineEdit_7.text()
        com_id = self.lineEdit_8.text()
        sql = f"UPDATE `Singer` SET `com_id` = '{com_id}' WHERE `SSN` ='{SSN}'"
        try:
            mycursor.execute(sql)
            mydb.commit()
            self.textBrowser.append(
                self.textBrowser.append(
                sql ))
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_8_click(self): # sql輸入法
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql_str = str(self.textEdit_35.toPlainText())
        first_word = sql_str.split()[0]

        if (first_word.lower() == "select"):
            try:
                mycursor.execute(sql_str)
                self.textBrowser.append(
                    sql_str)
                myresult = mycursor.fetchall()
                column_names = [i[0] for i in mycursor.description]

                self.set_table_widget(myresult, column_names)
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")
        else:
            try:
                mycursor.execute(sql_str)
                mydb.commit()
                self.textBrowser.append(
                    sql_str)
            except mysql.connector.Error as err:
                self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_9_click(self): # update album's ce_id
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        a_id = self.lineEdit_14.text()
        ce_id = self.lineEdit_15.text()
        if(ce_id.lower() == "null"):
            ce_id = None
        sql = f"UPDATE `Album` SET `ce_id` = '{ce_id}' WHERE `a_id` ='{a_id}'"
        try:
            mycursor.execute(sql)
            mydb.commit()
            self.textBrowser.append(self.textBrowser.append(sql))
        
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_10_click(self): # 查詢主持人為Anne的屆數 s-f-w 
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        sql = f"SELECT `ce_id` FROM `Ceremony` WHERE host_name = 'Anne'"
        try:
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            column_names = [i[0] for i in mycursor.description]
            self.set_table_widget(myresult, column_names)
            self.textBrowser.append(self.textBrowser.append(sql))
        
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def on_pushButton_11_click(self): # 驚曲獎因疫情取消 
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
        ce_id = self.lineEdit_24.text()
        sql = f"DELETE FROM `Ceremony` WHERE `ce_id` ='{ce_id}'"
        try:
            mycursor.execute(sql)
            self.textBrowser.append(self.textBrowser.append(sql))
        
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

if __name__ == '__main__':  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
