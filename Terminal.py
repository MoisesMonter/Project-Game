from typing import Dict
from config import Config_Menu
from Menu import *
import sys
import os

class MenuTerminal:
    def __init__(self,language):
        if language == 1:
            self.language = Config_Menu().loading_lang()  #Responsável pelas legendas
        else:
            self.language = Config_Menu().loading_lang()  #nas duas provaveis suposições tem que retorna 0 ou um, para todo caso, essas 4 linhas de codigo irão forçar isso acontecer mesmo contra vontade do usuario. Simples, sem linguagem, sem informação, sem informação sem codigo para interagir!

    def __str__(self,string):      #acessa os balões de informações da informação do personagem e Menu e Criação de personagem... para todos os casos feito com intuito de interagir com a pasta Create.py,Menu.py e info_person.py
        BallonInfo(self.language,string).Ballon()

    def Language(self):         #definir de forma rapida qual linguagem usar no programa, informação necessaria para se abrir uma pasta de arquivo, verificar sua existencia e depois retornar seu valor boleano no meio de um pequeno texto de informações
        self.language = Config_Menu().loading_lang()
        return self.language

    def infolist(self,tipe,string):             #definindo uma linguagem intrigante que estou fazendo testes para dar UP e futuramente pode  interagir com o nome dos itens do programa
        if tipe == 0:
            return InfoLists(self.language).LVLUP(string)

    def Action():
        return Damage().Action_Option()

    def limpesa_global(self):           #limpesa de tela, simplesmente um cls voltado tanto para Windows quanto para linux... Não faço ideia se funciona para Mac....
        os.system('cls' if os.name == 'nt' else 'clear')

from ballon import* #< hierarquia /\ não pode estar a cima
from info_person import * #< Hierarquia de poder tem que ficar a baixo do MenuTerminal
from info_list import* # Para Hierarquia funcionar  nos codigos tem que informar como se sua existencia viesse a baixo do codigo para Herança funcionar em cadeia


    
