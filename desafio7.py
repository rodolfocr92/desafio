#SQLite3 já é incorporada a biblioteca padrão do Python, recomendo o SQLiteStudio para
# leitura do banco de dados.

import sqlite3
import numpy as np


connection = sqlite3.connect('alunos.db')
c = connection.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados (DRE integer,Curso text,Nome text,Gênero text,Data text,Altura real,Peso real,CRA real,Créditos integer,Renda real)')

def inserir(dre,curso,nome,genero,data,altura,peso,cra,creditos,renda):
    c.execute('INSERT INTO dados (DRE,Curso,Nome,Gênero,Data,Altura,Peso,CRA,Créditos,Renda) VALUES (?,?,?,?,?,?,?,?,?,?)',(dre,curso,nome,genero,data,altura,peso,cra,creditos,renda))
    connection.commit()
       
def menu():
    print("Sistema de Ensino")
    print("Escolha uma opção: ")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Estatísticas")
    print("0 - Terminar")
    opcao = int(input("Entre com a opção desejada: "))
    return opcao

def contarGenero(genero):
    gen = 'SELECT * FROM dados WHERE Gênero = ?'
    cont = 0
    for i in c.execute(gen, (genero,)):
        cont += 1
    return cont
    
def stdd():
    select = c.execute('SELECT CRA FROM dados WHERE Curso = "Engenharia"')
    copy = select.fetchall()
    print("O desvio padrão do CRA dos alunos de Engenharia é: ", np.std(copy))

def cr():
    nome_cra = c.execute('SELECT Nome FROM dados WHERE (CRA > 6)')
    nome = nome_cra.fetchall()
    print(nome)
    
    


create_table()

if __name__ == "__main__":
    
    try:
        opcao = menu()
        while (opcao >= 0):
            if opcao == 1:
                try:
                    print('Cadastro Aluno')
                    dre = int(input("Digite o DRE do aluno: "))
                    curso = str(input("Digite o curso do aluno: "))
                    nome = str(input("Digite o nome do aluno: "))
                    genero = str(input("Digite o gênero do aluno: "))
                    data = str(input("Digite a data de nascimento do aluno: "))
                    altura = float(input("Digite a altura do aluno: "))
                    peso = float(input("Digite o peso do aluno: "))
                    cra = float(input("Digite o CRA do aluno: "))
                    creditos = int(input("Digite os créditos obtidos do aluno: "))
                    renda = float(input("Digite a renda do aluno: "))
                    
                    inserir(dre,curso,nome,genero,data,altura,peso,cra,creditos,renda)
                    print("Cadastrado com sucesso.")
                    
                except:
                    print('Erro ao cadastrar.')
                opcao = menu()
            elif opcao == 2:
                try:
                    print("Lista de alunos:")
                    sql = c.execute('SELECT * FROM dados')
                    rows = sql.fetchall()
                    for row in rows:
                        print(row)
                    
                except:
                    print("Erro ao listar.")                    
                opcao = menu()
            elif opcao == 3:
                print('Escolha a estatística desejada: ')
                print("1 - Quantidade de alunos do gênero feminino")
                print("2 - Quantidade de alunos do gênero masculino")
                print("3 - Média de CRA dos alunos do curso Engenharia")
                print("4 - Desvio padrão de CRA dos alunos do curso Engenharia")
                print("5 - Alunos CR > 6")
                print("6 - Média de altura dos alunos")

                est = int(input("Entre com a opção desejada: "))
                try:  
                    if est == 1:
                        print("A quantidade de alunos do gênero feminino é: ", contarGenero("F"))
                    elif est == 2:
                        print("A quantidade de alunos do gênero masculino é: ", contarGenero("M"))
                    elif est == 3:
                        c.execute('SELECT avg(CRA) FROM dados WHERE Curso = "Engenharia"')                    
                        print("A média de CRA dos alunos do curso Engenharia é: ", c.fetchone()[0])
                    elif est == 4:
                        stdd()
                    elif est == 5:
                        cr()
                    elif est == 6:
                        c.execute("SELECT avg(Altura) FROM dados")
                        print("A média de altura dos alunos é: ", c.fetchone()[0])
                    
                except:
                    print("Erro.")

                               
                opcao = menu()
            
            else:
                raise KeyboardInterrupt
                                       
    except KeyboardInterrupt:
        print('Programa finalizado por usuário.')
                
            
                
        
