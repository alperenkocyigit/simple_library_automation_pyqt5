import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sqlite3

class KitaplarForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle("Kitaplar")

        # Form elemanlarını oluştur
        self.lineEdit_kitap_adi = QtWidgets.QLineEdit()
        self.comboBox_kategori = QtWidgets.QComboBox()
        self.comboBox_yazar = QtWidgets.QComboBox()
        self.pushButton_ekle = QtWidgets.QPushButton("Ekle")
        self.pushButton_guncelle = QtWidgets.QPushButton("Güncelle")
        self.pushButton_sil = QtWidgets.QPushButton("Sil")
        self.tableWidget_kitaplar = QTableWidget()

        # Kategori ve yazar verilerini doldur
        self.load_kategori_yazar_data()

        # Layout oluştur
        layout = QVBoxLayout()
        layout.addWidget