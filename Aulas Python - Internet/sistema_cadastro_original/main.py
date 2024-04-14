import sys
from PyQt5 import QtWidgets, uic
import sqlite3

def cadastrar_novo_usuario(nome, email, senha, confirmar_senhas):
    erro = False

    if nome:
        pass

    if "@" in email and ".com":
        pass

    if senha == confirmar_senhas and len(senha) > 6:
        pass

    else:
        erro = True

    try:
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (nome text, email text, senha text)")
        cursor.execute(f"INSERT INTO data_user VALUES ('{nome}', '{email}', '{senha}')")

        banco.commit()
        banco.close()

    except sqlite3.Error as error:
        print(error)
        erro = True

    return erro

def logar_com_email_e_senha():
    email = janela.lineEdit.text()
    senha = janela.lineEdit_2.text()

    try:
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        cursor.execute(f"SELECT senha FROM data_user WHERE email='{email}'")

        senha_cap = cursor.fetchall()

        try:
            if senha == senha_cap[0][0]:
                print("Entrou")

            else:
                print("Não entrou")
        except:
            pass

    except sqlite3.Error as error:
        print(error)

    janela.lineEdit.setText("")
    janela.lineEdit_2.setText("")

app = QtWidgets.QApplication([])
janela = uic.loadUi("telas_do_projeto.ui")

janela.pushButton.clicked.connect(logar_com_email_e_senha) # sign in with email and password
janela.pushButton_2.clicked.connect(lambda: janela.gerenciador_telas.setCurrentWidget(janela.cadastro))

janela.show()
sys.exit(app.exec_())
