#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:53:42 2021

@author: hideosuzuki
"""

from modulos import *

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
    
    def variaveisCli(self):
        #get() serve para pegar o valor da entry
        self.codigo = self.codigo_entry.get();
        self.nome = self.nome_entry.get();
        self.telefone = self.telefone_entry.get();
        self.cidade = self.cidade_entry.get();
        
    
    #botao para adicionar clientes ao banco de dados
    def add_clientes(self):
        #chama as variaveis dos clientes
        self.variaveisCli()
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
    
    def ondoubleclick(self, event):
        #esta funcao serve para em duplo clique voltar as informacoes do cliente
        
        #limpa os entrys
        self.limpa_tela();
        #seleciona um cliente
        self.listaCli.selection()
        
        #pega as informacoes do cliente ja cadastrado
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, "values")
            
        self.codigo_entry.insert(END, col1)
        self.nome_entry.insert(END, col2)
        self.telefone_entry.insert(END, col3)
        self.cidade_entry.insert(END, col4)
    
    def deleta_cliente(self):
        #funcao serve para apagar o cliente
        #chama as variaveis dos clientes
        self.variaveisCli()
        self.conecta_bd()
        #codigo para deletar o cliente
        #print("imprimir ?", self.codigo)
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        
        self.conn.commit()        
        self.desconecta_bd()
        #limpa a tela
        self.limpa_tela()
        #atualiza a lista
        self.select_list()
    
    def altera_clientes(self):
        #funcao para alterar clientes
        #chama as variaveis dos clientes
        self.variaveisCli()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?,
                            telefone = ?, cidade = ? WHERE cod = ? """, 
                            (self.nome, self.telefone, self.cidade, self.codigo))
        
        self.conn.commit()        
        self.desconecta_bd()
        #limpa a tela
        self.limpa_tela()
        #atualiza a lista
        self.select_list()
    
    def busca_cliente(self):
        #buscar o clientes
        
        self.conecta_bd()
        #limpar a lista
        self.listaCli.delete(*self.listaCli.get_children())
        
        #procurar o nome, O % serve para buscar que estiver a mais no nome
        self.nome_entry.insert(END,"%")
        nome = self.nome_entry.get()
        
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes WHERE nome_cliente like '%s' ORDER BY nome_cliente ASC""" % nome)
        
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("",END, values=i)
        
        #limpa a tela
        self.limpa_tela()
        
        self.desconecta_bd()
        
