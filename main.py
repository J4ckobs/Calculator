#Jakub Flis 418310
#Elektronika rok 1
#Python 3.9

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

#główna klasa okna aplikacji okienkowej
class App(QWidget):
    def __init__(self):
        super().__init__()
        #określanie parametrów okna aplikacji
        self.title = 'Kalkulator'
        self.left = 1300 # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 300 # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 340 # szerokośc okna
        self.height = 420 # wysokość okna
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)

        #pierwsze pole tekstowe
        self.textbox1 = QLineEdit("", self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(300, 40)
        self.textbox1.setReadOnly(True)
        self.textbox1.setAlignment(Qt.AlignRight)
        self.textbox1.setTextMargins(0, 0, 10, 0)

        #drugie pole tekstowe
        self.textbox2 = QLineEdit("", self)
        self.textbox2.move(20, 70)
        self.textbox2.resize(300, 40)
        self.textbox2.setReadOnly(True)
        self.textbox2.setAlignment(Qt.AlignRight)
        self.textbox2.setTextMargins(0, 0, 10, 0)

        #trzecie pole tekstowe (tutaj będą wyświetlały się wyniki)
        self.textbox3 = QLineEdit("", self)
        self.textbox3.move(20, 120)
        self.textbox3.resize(300, 40)
        self.textbox3.setReadOnly(True)
        self.textbox3.setAlignment(Qt.AlignRight)
        self.textbox3.setTextMargins(0, 0, 10, 0)

        #zmienna określająca stan i pozycje w której aktualnie jesteśmy (pole 1, 2, lub 3)
        self.status = 0
        #zmienna opisująca jaka operacja na liczbach ma byc wykonana
        self.operation = ''

        #sekcja numeryczna (przyciski tworzone za pomocą funkcji init_button)
        self.init_button("b7", "7", 20, 170, self.on_click_num)

        self.init_button("b8", "8", 80, 170, self.on_click_num)

        self.init_button("b9", "9", 140, 170, self.on_click_num)

        self.init_button("b4", "4", 20, 230, self.on_click_num)

        self.init_button("b5", "5", 80, 230, self.on_click_num)

        self.init_button("b6", "6", 140, 230, self.on_click_num)

        self.init_button("b1", "1", 20, 290, self.on_click_num)

        self.init_button("b2", "2", 80, 290, self.on_click_num)

        self.init_button("b3", "3", 140, 290, self.on_click_num)

        self.init_button("b0", "0", 20, 350, self.on_click_num)

        #sekcja pozostałych przycisków (operatorów działań, 'równa sie' oraz czyszczenie pól,
        # przyciski również tworzone za pomocą funckji init_button)
        self.init_button("plus", "+", 200, 170, self.on_click_char)

        self.init_button("minus", "-", 200, 230, self.on_click_char)

        self.init_button("mnoz", "*", 200, 290, self.on_click_char)

        self.init_button("dziel", "/", 200, 350, self.on_click_char)

        self.init_button("pow", "x^2", 80, 350, self.on_click_sq_pw)

        self.init_button("sqrt", "√x", 140, 350, self.on_click_sq_pw)

        self.init_button("CE", "CE", 260, 170, self.on_click_clear)

        self.init_button("C", "C", 260, 230, self.on_click_clear)

        self.init_button("equal", "=", 260, 290, self.on_click_out, 50, 110)

        #pokazuje/wyświetla graficzny interfejs aplikacji
        self.show()
    #funkcja służąca do tworzenia i nadaniu właściwych parametrów przyciskom
    def init_button(self, b, text, x, y, clck_event, x_size=50, y_size=50):
        b = QPushButton(text, self)
        b.move(x, y)
        b.resize(x_size, y_size)
        b.clicked.connect(clck_event)
    #funkcja odpowiedzialna za reakcje na wciśnięcie przycisku z sekcji numerycznej
    def on_click_num(self):
        if self.status == 0:
            text = self.textbox1.text() + self.sender().text()
            self.textbox1.setText(text)
        if self.status == 1:
            text = self.textbox2.text() + self.sender().text()
            self.textbox2.setText(text)
    #funkcji odpowiedzialna za reakcje na wciśnięcie przycisku operacji (mnożenia, dzielenia, dodawania, odejmowania)
    def on_click_char(self):
        if self.sender().text() == "-" and self.status == 0 and self.textbox1.text() == "":
            self.textbox1.setText("-" + self.textbox1.text())
        else:
            if self.textbox1.text() != '-' and self.textbox1.text() != '':
                self.operation = self.sender().text()
                self.status = 1

    #funkcja odpowiadająca za wykonanie potęgowania i pierwiastkowania
    def on_click_sq_pw(self):
        if self.sender().text() == "√x":
            if int(self.textbox1.text()) < 0:
                self.textbox3.setText("Błędna wartość")
            else:
                a = math.sqrt(int(self.textbox1.text()))
                self.textbox3.setText(str(a))
        elif self.sender().text() == "x^2":
            a = math.pow(int(self.textbox1.text()), 2)
            self.textbox3.setText(str(a))
        self.status = 2
    #funkcja wykonuje sie w momencie wciśnięcia przycisku równa się
    def on_click_out(self):
        #gdy pierwsze i drugie pole tekstowe nie są równe zero wykona się dalsza część instrukcji
        # odpowiedzialnych za dokonanie obliczeń
        if self.textbox1.text() != "" and self.textbox2.text() != "":
            self.status = 2
            t1 = int(self.textbox1.text())
            t2 = int(self.textbox2.text())
            if self.operation == "*":
                t3 = t1*t2
                self.textbox3.setText(str(t3))
            if self.operation == "/":
                # zabezpieczenie sprawdzające czy nie dzielimy przez 0
                if int(self.textbox2.text()) == 0:
                    if int(self.textbox1.text()) == 0:
                        self.textbox3.setText("Wartość nie określona")
                    else:
                        self.textbox3.setText("Nie można dzielić przez zero")
                else:
                    t3 = t1/t2
                    self.textbox3.setText(str(t3))
            if self.operation == "+":
                t3 = t1+t2
                self.textbox3.setText(str(t3))
            if self.operation == "-":
                t3 = t1-t2
                self.textbox3.setText(str(t3))
    #funkcja wykonuje siegdy wciśniemy 'CE' lub 'C' odpowiedzialna za wyczyszczenie pól z wartości
    # i przygotowanie ich do ponownego wykonania obliczeń
    def on_click_clear(self):
        if self.sender().text() == "CE":
            if self.status == 0:
                self.textbox1.setText("")
                return
            if self.status == 1:
                if self.textbox2.text() != '':
                    self.textbox2.setText("")
                else:
                    self.status = 0
                    self.textbox1.setText("")
                return
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.status = 0

#utworzenie i wywołanie klasy aplikacji
app = QApplication(sys.argv)
ex = App()
app.exec_()
    #wprowadzić komentarze, sprawdzić poprawność nazewnictwa ect.
