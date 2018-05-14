import sys
from backend import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Simulador de Gerência de Memória'
        self.width = 480
        self.height = 650
        self.top = 10
        self.left = 10
        self.paginas = 5
        self.pagemiss = 0
        self.pagehit = 0
        self.pid = 0
        self.local_page = []
        self.bk = Backend()
        self.initUI()
    
    def initUI(self):
        # Inicia a Janela
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Texto Páginas
        self.lbl = QLabel(self)
        self.lbl.setText('Páginas')
        self.lbl.move(20, 15)

        # Cria as Caixas de Texto das paginas
        self.textbox_1 = QLineEdit(self)
        self.textbox_1.move(20, 45)
        self.textbox_1.resize(40,80)

        self.textbox_2 = QLineEdit(self)
        self.textbox_2.move(62, 45)
        self.textbox_2.resize(40,80)

        self.textbox_3 = QLineEdit(self)
        self.textbox_3.move(104, 45)
        self.textbox_3.resize(40,80)

        self.textbox_4 = QLineEdit(self)
        self.textbox_4.move(146, 45)
        self.textbox_4.resize(40,80)

        self.textbox_5 = QLineEdit(self)
        self.textbox_5.move(188, 45)
        self.textbox_5.resize(40,80)

        self.textbox_6 = QLineEdit(self)
        self.textbox_6.move(230, 45)
        self.textbox_6.resize(40,80)

        # Texto Quadros
        self.lbl = QLabel(self)
        self.lbl.setText('Quadros')
        self.lbl.move(20, 150)

        # Cria as Caixas de Texto dos quadros
        self.textbox_q1 = QLineEdit(self)
        self.textbox_q1.move(20, 180)
        self.textbox_q1.resize(40,80)

        self.textbox_q2 = QLineEdit(self)
        self.textbox_q2.move(62, 180)
        self.textbox_q2.resize(40,80)

        self.textbox_q3 = QLineEdit(self)
        self.textbox_q3.move(104, 180)
        self.textbox_q3.resize(40,80)

        self.textbox_q4 = QLineEdit(self)
        self.textbox_q4.move(146, 180)
        self.textbox_q4.resize(40,80)

        self.textbox_q5 = QLineEdit(self)
        self.textbox_q5.move(188, 180)
        self.textbox_q5.resize(40,80)

        self.textbox_q6 = QLineEdit(self)
        self.textbox_q6.move(230, 180)
        self.textbox_q6.resize(40,80)

        self.textbox_q7 = QLineEdit(self)
        self.textbox_q7.move(272, 180)
        self.textbox_q7.resize(40,80)

        self.textbox_q8 = QLineEdit(self)
        self.textbox_q8.move(314, 180)
        self.textbox_q8.resize(40,80)

        # Texto Processo
        self.lbl = QLabel(self)
        self.lbl.setText('Criar Processo')
        self.lbl.move(20, 285)

        # Cria Botão de Criação De processo
        self.button_4k = QPushButton('Processo 4K', self)
        self.button_4k.move(20, 315)
        self.button_4k.clicked.connect(self.AdicionaProcesso4K)

        self.button_8k = QPushButton('Processo 8K', self)
        self.button_8k.move(130, 315)
        self.button_8k.clicked.connect(self.AdicionaProcesso8K)

        self.button_12k = QPushButton('Processo 12K', self)
        self.button_12k.move(240, 315)
        self.button_12k.clicked.connect(self.AdicionaProcesso12K)

        # Texto Pular Ciclos
        self.lbl = QLabel(self)
        self.lbl.setText('Pular Ciclo')
        self.lbl.move(20, 380)

        # Cria Botão de Skip cycles
        self.button_skip1 = QPushButton('Pular 1 Ciclo', self)
        self.button_skip1.move(20, 410)
        self.button_skip1.clicked.connect(self.Avanca1)

        self.button_skip2 = QPushButton('Pular 2 Ciclos', self)
        self.button_skip2.move(130, 410)
        self.button_skip2.clicked.connect(self.Avanca2)

        self.button_skip3 = QPushButton('Pular 3 Ciclos', self)
        self.button_skip3.move(240, 410)
        self.button_skip3.clicked.connect(self.Avanca3)

        # Texto Kill Process
        self.lbl = QLabel(self)
        self.lbl.setText('Matar Processo')
        self.lbl.move(20, 475)

        # Texto PID
        self.lbl = QLabel(self)
        self.lbl.setText('Digite o PID do processo')
        self.lbl.move(25, 500)
        self.lbl.resize(300,20)

        # TextBox do PID
        self.textbox_kill = QLineEdit(self)
        self.textbox_kill.move(20, 525)
        self.textbox_kill.resize(160,30)

        # Cria Botão de Matar Processo
        self.button_kill = QPushButton('Matar', self)
        self.button_kill.move(190, 525)
        self.button_kill.resize
        self.button_kill.clicked.connect(self.MataProcesso)

        # Cria Botão de Ajuda
        self.button_help = QPushButton('Ajuda', self)
        self.button_help.move(370, 15)
        self.button_help.resize
        self.button_help.clicked.connect(self.Ajuda)

        # Texto PID Anterior
        self.lbl_pidAnt = QLabel(self)
        self.lbl_pidAnt.setText('PID Ant.: ' + str(self.pid))
        self.lbl_pidAnt.move(390, 190)

        # Texto PID Atual
        self.lbl_pidAtual = QLabel(self)
        self.lbl_pidAtual.setText('PID Atual: ' + str(self.pid))
        self.lbl_pidAtual.move(390, 205)

        # Texto PID Prox
        self.lbl_pidProx = QLabel(self)
        self.lbl_pidProx.setText('PID Prox.: ' + str(self.pid))
        self.lbl_pidProx.move(390, 220)

        # Texto Page Hit
        self.lbl_pagehit = QLabel(self)
        self.lbl_pagehit.setText('Page Hit: ' + str(self.pagehit))
        self.lbl_pagehit.move(20, 120)

        # Texto Page Miss
        self.lbl_pagemiss = QLabel(self)
        self.lbl_pagemiss.setText('Page Miss: ' + str(self.pagemiss))
        self.lbl_pagemiss.move(100, 120)

        # Texto Criadores
        self.lbl_textoCriadores = QLabel(self)
        self.lbl_textoCriadores.setText('Felipe Homrich Melchior - Lucas Antunes de Almeida')
        self.lbl_textoCriadores.move(70, 620)
        self.lbl_textoCriadores.resize(500, 20)

        self.show()

    def setPid(self, pid1, pid2, pid3):
        self.lbl_pidAnt.setText('PID Ant.: ' + str(pid1))
        self.lbl_pidAtual.setText('PID Atual: ' + str(pid2))
        self.lbl_pidProx.setText('PID Prox.: ' + str(pid3))

        self.repaint()

    def PageHit(self, pagehit):
        self.lbl_pagehit.setText('Page Miss: ' + str(pagehit))
        self.repaint()

    def PageMiss(self, pagemiss):
        self.lbl_pagemiss.setText('Page Miss: ' + str(pagemiss))
        self.repaint()

    def UpdatePage(self):
        self.frames = self.bk.setFrames()    
        self.local_page = self.bk.actualPage() 

        self.textbox_1.setText("   " + str(self.local_page[0]))
        self.textbox_2.setText("   " + str(self.local_page[1]))
        self.textbox_3.setText("   " + str(self.local_page[2]))
        self.textbox_4.setText("   " + str(self.local_page[3]))
        self.textbox_5.setText("   " + str(self.local_page[4]))
        self.textbox_6.setText("   " + str(self.local_page[5]))

        self.local_missHit = self.bk.missAndHit()
        self.PageHit(self.local_missHit[0])
        self.PageMiss(self.local_missHit[1])

        self.local_pids = self.bk.getPids()
        self.setPid(self.local_pids[0], self.local_pids[1], self.local_pids[2])

    @pyqtSlot()
    def AdicionaProcesso4K(self):
        self.bk.createProcess(4)
        self.bk.setPages()
        self.Avanca1()

    def AdicionaProcesso8K(self):
        self.bk.createProcess(8)
        self.bk.setPages()
        self.Avanca1()

    def AdicionaProcesso12K(self):
        self.bk.createProcess(12)
        self.bk.setPages()
        self.Avanca1()

    def MataProcesso(self):
        self.PID_to_kill = self.textbox_kill.text()
        
        self.bk.killProcess(self.PID_to_kill)
        
        print(self.PID_to_kill)
    
    def Avanca1(self):
        self.UpdatePage()

    def Avanca2(self):
        self.Avanca1()
        self.Avanca1()

    def Avanca3(self):
        self.Avanca1()
        self.Avanca1()
        self.Avanca1()

    def Ajuda(self):
        QMessageBox.question(self, "Ajuda", "TODO", QMessageBox.Ok)
