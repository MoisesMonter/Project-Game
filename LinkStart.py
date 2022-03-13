from typing import Dict
from config import Config_Menu
from Menu import *
from Terminal import * #teminal é responsável
from ballon import* #< hierarquia /\ não pode estar a cima
from info_person import * #< Hierarquia de poder tem que ficar a baixo do MenuTerminal
from info_list import* # Para Hierarquia funcionar  nos codigos tem que informar como se sua existencia viesse a baixo do codigo para Herança funcionar em cadeia
from Point import *


if __name__ == "__main__":
    MenuTerminal(0).limpesa_global() #responsável por ver se existe um arquivo chaamado <config.txt> caso não exista irá gerar um com informações contidas
    Config_Menu().conf_languages() #verifica se existe algum texto dentro caso contrario implementará com Zero
    language = MenuTerminal(Config_Menu().loading_lang()).Language() #informação 0/1 é importante para declarar que o jogo inicialize já PT/ING

     #"FAÇA ISSO?" ele abre um menu com as informações necessárias
    persona = int(Initial_Menu(0).Do_it())
    Dictlocal = {}
    Dictlocal = Person(language,persona).alocate_info()
    if persona <= 0:
        sys.exit(0)
    MenuTerminal(0).limpesa_global()
     #um Dicionario vasio
 #pegar todas as informações e tranformar em um dicts
    while  0 < persona:
        if Dictlocal['Point'] == '0':
            Dictlocal = PointHistory(language,**Dictlocal).historypoint()
        if Dictlocal['Point'] == '1':
            Dictlocal = PointHistory(language,**Dictlocal).historypoint()
        MenuTerminal(language).__str__('linkstart')
        x = int(input())
        if  x == int(1):
            Dictlocal = Person(language,persona).save_info(**Dictlocal)
        if  x == int(2):
            Dictlocal = Person(language,persona).save_info(**Dictlocal)
            MenuTerminal(0).limpesa_global()
            persona = int(Initial_Menu(0).Do_it())
            del Dictlocal
            Dictlocal = {}
            Dictlocal = Person(language,persona).alocate_info()
        
