#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:53:27 2021

@author: hideosuzuki
"""

from modulos import *
class Relatorios():
    def printCliente(self):
        #abrir o navegador e a mostrar o relatorio
        print("chama webbrowser")
        webbrowser.open("cliente.pdf")
        
    def geraRelatorioCliente(self):
        #salva no nome do arquivo
        self.c = canvas.Canvas("cliente.pdf")
        
        #pega as variaveis para imprimir
        self.codigoRel = self.codigo_entry.get()
        self.nomeoRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        
        #setar a fonte do pdf
        self.c.setFont("Helvetica-Bold",24)
        #imprimir uma variavel string, posicao esq para direita
        #A4 ˜500 da esquerda (0) para direita (500)
        #A4 ˜800 de baixo (0) para cima (800)
        self.c.drawString(200, 790, "Nome do Cliente")
        
        self.c.setFont("Helvetica-Bold",18)
        self.c.drawString(50, 700, "Código: ")
        self.c.drawString(50, 650, "Nome: ")
        self.c.drawString(50, 600, "Telefone: ")
        self.c.drawString(50, 550, "Cidade: ")
        
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 650, self.nomeoRel)
        self.c.drawString(150, 600, self.telefoneRel)
        self.c.drawString(150, 550, self.cidadeRel)
        
        #criar moldura quadrada
        self.c.rect(30, 500, 500, 330, fill= False,stroke = True)
        #cria linhas
        self.c.rect(30, 400, 500, 3, fill= True,stroke = True)
        
        #mostrar a pagina
        self.c.showPage()
        #salva o arquivo
        self.c.save()
        #exibe o arquivo
        self.printCliente()
    
