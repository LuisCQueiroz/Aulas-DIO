import sys
from PyQt5 import uic, QtWidgets


import sqlite3

#def cadastrar_novo_usuario(nome, email, senha, confirmar_senhas):
def cadastrar_novo_usuario():
    nome = janela.lineEdit_3.text()
    email = janela.lineEdit_5.text()
    senha = janela.lineEdit_4.text()
    confirmar_senhas = janela.lineEdit_6.text()

    erro = False

    # Passo 1: Validar as Informações do cadastro
    if nome:
        pass

    if "@" in email and ".com":
        pass

    if senha == confirmar_senhas and len(senha) > 6:
        pass

    else:
        erro = True


    # Passo 2: Criar e se conectar com o banco de dados
    try:
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user(nome text,email text, senha text)")
        cursor.execute(f"INSERT INTO data_user VALUES('{nome}', '{email}', '{senha}')")

        banco.commit()
        banco.close()
        print("Dados inseridos com sucesso ! ")

        janela.lineEdit_3.setText("")
        janela.lineEdit_5.setText("")
        janela.lineEdit_4.setText("")
        janela.lineEdit_6.setText("")


    except sqlite3.Error as error:
        print("Erro ao inserir os dados: ",error)
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


    # Passo 3 : Inserir as informações do usuário no banco
#
# if cadastrar_novo_usuario("Luis", "teste@gmail.com", "teste123", "teste"):
#     print("Cadastro ok")
# else:
#     print("Cadastro com Erro!!!")

app = QtWidgets.QApplication([])
janela = uic.loadUi("interface_login.ui")

janela.pushButton.clicked.connect(logar_com_email_e_senha) # sign in with email and password
janela.pushButton_4.clicked.connect(lambda: janela.gerenciador_telas.setCurrentWidget(janela.cadastro))
janela.pushButton_3.clicked.connect(cadastrar_novo_usuario)

janela.show()
sys.exit(app.exec_())
