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

'''if __name__ == "__main__":
    MenuTerminal(0).limpesa_global()

    Config_Menu().conf_languages()
    language = MenuTerminal(Config_Menu().loading_lang()).Language()
    i = Initial_Menu(0).Do_it()
    if i == 4:
        sys.exit(0)
    MenuTerminal(0).limpesa_global()
    print("ACCOUNT-",i,"-LINK START!")
    Dictlocal={}
    Dictlocal = Person(language,i).alocate_info()
    #Dictlocal = Set(language,**Dictlocal).acess_status()
    Dictlocal = Set(language,**Dictlocal).acess_backpack()
    
    x = input("você encontra o primeiro monstro...decide atacar:(s/n)")
    if x == 's':
        print("Ele bateu em você...")
        Dictlocal = UP(language,**Dictlocal).STS('Hp','60')
        #Dictlocal.update({'Hp':'-20'})
        print("você usou magia E DEU CRITICO..")
        Dictlocal = UP(language,**Dictlocal).STS('Mp','35')
        print("Nossa você conseguiu !!100!! bônus de experiencia. Parabéns")
        Dictlocal = UP(language,**Dictlocal).STS('Xp','100')

        #Dictlocal.update({'Xp':'20'})
        x =input("Ele deixou cair uma espada enferrujada...Deseja pega-lo(s/n):")
        if x == 's' or x=='S':
            Dictlocal = Set(language,**Dictlocal).take('6_right11')
            print("Vamos ver como está teus status!\n")
            Dictlocal = Set(language,**Dictlocal).acess_status()
    else:
        print("você foge...")
        #Dictlocal = SET(**Dictlocal).BP()
    x =input("Deseja acessar seu Set(s/n)::")
    if x =='s' or x=='S' or x==1:
        Dictlocal = Set(language,**Dictlocal).acess_set()



    x = input("Você Deseja ver suas informações?:(s/n)!")
    if x =='s':
        print("SUAS INFORMAÇÕES ESTÃO CONTIDAS EM UM DICTIONARY: VEJAZ>\n",Dictlocal)
    elif x =='n':
        print("você decidiu não ver...")
    print("okay")
    
    Dictlocal= Person(language,i).save_info(**Dictlocal)
    print("<Salvo>\n")'''

    


    
