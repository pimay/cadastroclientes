#tutorial sobre tkinter htt.ps://www.youtube.com/watch?v=RtrZcoVD1WM

from tkinter import *
from tkinter import ttk
import sqlite3

#variavel para chamar o tkinter
root = Tk();

#classe com as funcoes dos botoes - back end
class Funcs():
    #nao vai precisar de init pq nao vai precisar nada automaticamente
    def limpa_tela(self):
        #pegar o nome das entry
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    ###BANCO DE DADOS##
    #funcao para conectar ao banco de dados
    def conecta_bd(self):
        #nome do banco de dados
        self.conn = sqlite3.connect("clientes.db")
        #variavel
        self.cursor = self.conn.cursor(); print("connectando ao banco de dados")
    
    #desconetar banco de dados
    def desconecta_bd(self):
        self.conn.close();  print("desconecta no banco de dados")
    
    def montaTabelas(self):
        #conectar o banco de dados
        self.conecta_bd(); 
        
        #criando a tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(48) NOT NULL,
            telefone INTERGER(20),
            cidade CHAR(40)                            
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    ###BANCO DE DADOS##
    
    #botao para adicionar clientes ao banco de dados
    def add_clientes(self):
        #get() serve para pegar o valor da entry
        self.codigo = self.codigo_entry.get();
        self.nome = self.nome_entry.get();
        self.telefone = self.telefone_entry.get();
        self.cidade = self.cidade_entry.get();
        
        #conecta ao banco de dados
        self.conecta_bd()
        #insere o valor
        self.cursor.execute(""" 
            INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.conn.commit();
        self.desconecta_bd();
        #para atualizar a lista anterior
        self.select_list();
        #limpa as entry
        self.limpa_tela();
    
    def select_list(self):
        #sempre chama a funcao delete
        self.listaCli.delete(*self.listaCli.get_children())
        #abre o banco de dados
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
                                    ORDER BY nome_cliente ASC;""")
                                    
        #a for list para jogar corretamente na treeview
        for i in lista:
            self.listaCli.insert("", END, values=i)
    
        self.conn.commit();
        
#classe da tela - front end
class Application(Funcs):
    def __init__(self):
        #equivalencia de nomes
        self.root = root;
        #chama a tela
        self.tela();
        #frames de tela
        self.frames_da_tela();
        #chama os botoes
        self.widgets_frame1();
        #lista de clientes
        self.lista_frame2();
        #montar a tabela
        self.montaTabelas();
        #sempre que abrir, mostra a lista
        self.select_list();
        #abre a janela
        root.mainloop();

    def tela(self):
        self.root.title("cadastro de clientes")
        #chama o background
        self.root.configure(background="#1e3743")
        #geometria inicial
        self.root.geometry("768x588")
        #define responsiva de tamanho
        self.root.resizable(True, True)
        #coloca o maximo e minimo tamanho de tela
        self.root.maxsize(width = 900, height = 700)
        self.root.minsize(width = 600, height = 400)
    
    def frames_da_tela(self):
        #define a divisao da tela 
        #self frame 1
        #bd border largura de background
        #bg - cor do background
        #highlightbackground - cor do highlight 
        #highlightthickness - largura do border
        self.frame_1 = Frame(self.root, bd = 4, bg = "#dfe3ee", 
                             highlightbackground = "#759feb", 
                             highlightthickness =3)
        #e proporcional a tela relx rely vao de 0-1
        self.frame_1.place(relx = .02, rely =.02, relwidth = 0.96, relheight = 0.46)
        
        
        #self frame 2
        self.frame_2 = Frame(self.root, bd = 4, bg = "#dfe3ee", 
                             highlightbackground = "#759feb", 
                             highlightthickness =3)
        #e proporcional a tela relx rely vao de 0-1
        self.frame_2.place(relx = .02, rely =.5, relwidth = 0.96, relheight = 0.46)
        
    def widgets_frame1(self):
        #botao limpar
        self.bt_limpar = Button(self.frame_1, text = "Limpar", bd = 2, bg="blue", fg = "black",
                                font=("verdana",8, "bold"),command = self.limpa_tela)
        #posicao
        self.bt_limpar.place(relx = 0.2, rely= 0.1, relwidth = .1, relheight = 0.15)
        
        #botao buscar
        self.bt_buscar = Button(self.frame_1, text = "Buscar", bd = 2, bg="blue", fg = "black",
                               font=("verdana",8, "bold"))
        #posicao
        self.bt_buscar.place(relx = 0.3, rely= 0.1, relwidth = .1, relheight = 0.15)
        
        #botao novo
        self.bt_novo = Button(self.frame_1, text = "Novo", bd = 2, bg="blue", fg = "black",
                              font=("verdana",8, "bold"),command = self.add_clientes)
        #posicao
        self.bt_novo.place(relx = 0.6, rely= 0.1, relwidth = .1, relheight = 0.15)
        
        #botao alterar
        self.bt_alterar = Button(self.frame_1, text = "Alterar", bd = 2, bg="blue", fg = "black",
                                font=("verdana",8, "bold"))
        #posicao
        self.bt_alterar.place(relx = 0.7, rely= 0.1, relwidth = .1, relheight = 0.15)
        
        #botao apagar
        self.bt_apagar = Button(self.frame_1, text = "Apagar", bd = 2, bg="blue", fg = "black",
                                font=("verdana",8, "bold"))
        #posicao
        self.bt_apagar.place(relx = 0.8, rely= 0.1, relwidth = .1, relheight = 0.15)
        ########################################################################################
        #criando Labels e Entry - Codigo
        self.lb_codigo = Label(self.frame_1, text = "Código", bg="#dfe3ee", fg = "black",
                                font=("verdana",8, "bold"))
        self.lb_codigo.place(relx =0.05, rely = 0.05)
    
        #criando uma entry
        self.codigo_entry = Entry(self.frame_1);
        self.codigo_entry.place(relx =0.05, rely = 0.15, relwidth = 0.08)
    
        #criando Labels e Entry - Nome
        self.lb_nome = Label(self.frame_1, text = "Nome", bg="#dfe3ee", fg = "black",
                                font=("verdana",8, "bold"))
        self.lb_nome.place(relx =0.05, rely = 0.35)
    
        #criando uma entry
        self.nome_entry = Entry(self.frame_1);
        self.nome_entry.place(relx =0.05, rely = 0.45, relwidth = 0.8)
        
        
        #criando Labels e Entry - Telefone
        self.lb_telefone = Label(self.frame_1, text = "Telefone", bg="#dfe3ee", fg = "black",
                                font=("verdana",8, "bold"))
        self.lb_telefone.place(relx =0.05, rely = 0.6)
    
        #criando uma entry
        self.telefone_entry = Entry(self.frame_1);
        self.telefone_entry.place(relx =0.05, rely = 0.7, relwidth = 0.4)
        
    
         #criando Labels e Entry - Cidade
        self.lb_cidade = Label(self.frame_1, text = "Cidade", bg="#dfe3ee", fg = "black",
                                font=("verdana",8, "bold"))
        self.lb_cidade.place(relx =0.5, rely = 0.6)
    
        #criando uma entry
        self.cidade_entry = Entry(self.frame_1);
        self.cidade_entry.place(relx =0.5, rely = 0.7, relwidth = 0.4)
        
    def lista_frame2(self):
        #lista  de clientes no frame 2
        #height - numero de linhas
        #column - colunas
        self.listaCli = ttk.Treeview(self.frame_2, column=("col1", "col2", "col3", "col4"))
        #coluna 1 ézero invisivel
        self.listaCli.heading("#0", text="")
        #coluna 2 
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        #especificacao do  - o total e´˜500
        self.listaCli.column("#0",width=1)
        self.listaCli.column("#1",width=50)
        self.listaCli.column("#2",width=200)
        self.listaCli.column("#3",width=125)
        self.listaCli.column("#4",width=125)
        #posicao das colunas
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        #barra de rolagem
        self.scrollLista = Scrollbar(self.frame_2, orient ="vertical", command=self.listaCli.yview)
        self.listaCli.config(yscrollcommand = self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth = 0.04, relheight = 0.85)
     
    
    
#call the class
Application()

